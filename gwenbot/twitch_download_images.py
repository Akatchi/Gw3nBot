import requests
import sys
import os

# get the twtich emotes api
import json

twitch_emotes = requests.get("https://twitchemotes.com/api_cache/v2/global.json").json()
# get the arguments
arguments = sys.argv
arguments.remove(arguments[0])


def get_twitch_images(*args):
    for twitch_emote in twitch_emotes['emotes']:
        # Get the image id from the api
        image_id = twitch_emotes['emotes'][twitch_emote]['image_id']

        # get the image template url
        image_url = twitch_emotes['template'][args[0][1]]  # change this to small / medium / large

        # download the image
        image_request = requests.get(image_url.format(image_id=image_id), stream=True)

        if args[0][1] == 'small':
            size = '1'
        elif args[0][1] == 'medium':
            size = '2'
        elif args[0][1] == 'large':
            size = '3'

        # save the image
        with open('images/twitch_emotes/'+size+'/' + twitch_emote.lower() + ".png", 'wb') as image:
            for chunk in image_request.iter_content(10):
                image.write(chunk)


def get_twitch_descriptions():
    data_list = {}

    for twitch_emote in twitch_emotes['emotes']:
        # get the description
        description = twitch_emotes['emotes'][twitch_emote]['description']

        data_list[twitch_emote.lower()] = description

    # start writing in the file
    with open('images/twitch_emotes/descriptions.json', mode='w', encoding='UTF-8') as file:
        json.dump(data_list, file)


if len(arguments) == 0:
    print("Missing args: <command> <size>")
    print("Commands: images, description")
    print("Size: small, medium, large")

elif len(arguments) == 1:
    # getting the description
    get_twitch_descriptions()

elif len(arguments) == 2:
    get_twitch_images(arguments)

