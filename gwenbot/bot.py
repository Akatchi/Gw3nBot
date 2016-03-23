import os
import time
import telepot
import logging

import config
from factory import CommandFactory


class TelegramBot(telepot.Bot):
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        logging.info("Got a chat message: [content_type: {}] [chat_type: {}] [chat_id: {}] [msg: {}]"
              .format(content_type, chat_type, chat_id, msg))

        # Sometimes the content_type is not text.
        # The bot can (at the moment) only process text messages
        if not content_type == 'text':
            raise NotImplementedError

        # If the user who send this message is blacklisted we will send them the default blacklisted message
        if msg['from']['username'] in config.blacklisted_usernames:
            logging.warning("Someone from the blacklist is trying to send a message! Here are the details: {}"
                .format(msg))

            bot.sendMessage(msg['chat']['id'], config.blacklisted_message)
        else:
            # User is not blacklisted so can send the message

            # Get the given command for the received message
            command = CommandFactory.get_command(msg['text'])

            if command is not None:
                command.execute(bot, msg)

            # TODO if we could not find a command model try a lookup in the database to retrieve the command


bot = TelegramBot('152064553:AAGjuBPWzT-j_hM5C-YLGoNxY2xp1nGQ3G0')  #os.environ.get('TOKEN'))
bot.notifyOnMessage()

# Configure the logging:
logging.basicConfig(filename='bot.log',level=logging.INFO)

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)