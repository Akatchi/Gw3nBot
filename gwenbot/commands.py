import sys
from random import randint

import requests
import config


class Command(object):
    """
    The constructor of the command object.
    """

    def __init__(self, query=None, description=None):
        self.query = query
        self.description = description

    """
    The query is the keyword that triggers the command (for example /help)
    This can also be a list to contain multiple aliases which will trigger the command
    """

    def get_query(self):
        return self.query

    """
    This method can be used by helper classes (for example the CommandLoader) to get the 'normalized' query
    key which can abe used for ordering a list of objects.

    This method transfers lists to a string by sorting the string and then taking the first element from the string
    to make all the objects for the sorting method of the same instance (string)
    """

    def get_sorting_key(self):
        sorting_key = self.query

        if isinstance(sorting_key, list):
            # If the sorting key is a list we will return the first (sorted) item from the list
            # which can be used as sorting key
            sorting_key = sorted(sorting_key)[0]

        return sorting_key

    """
    The description will be used by for example the /help command.
    It describes that the command does
    """

    def get_description(self):
        return self.description

    """
    This method needs to be overriden by the subclasses. It contains the action
    that the command can execute

    It takes a telepot.Bot as optional parameter. This bot will
    be used to send commands back to the bot

    The constructor also takes a msg object as option parameter.
    This contains the information about the received message
    """

    def execute(self, bot=None, msg=None, *args, **kwargs):
        raise NotImplementedError("A subclass must implement this abstract method!")


class HelpCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/help"
        self.description = "A list containing all commands."

    def execute(self, bot, msg, *args, **kwargs):
        help_text = 'Here are all my commands: \n\n'

        for command in CommandLoader().load_commands():
            help_text += "{} - {}\n".format(command.query, command.description)

        bot.sendMessage(msg['chat']['id'], help_text)


class ShrugCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/shrug"
        self.description = "¯\\_(ツ)_/¯"

    def execute(self, bot, msg, *args, **kwargs):
        # If we have additional arguments obtain them
        additional_args = get_additional_arguments(self)

        bot.sendMessage(msg['chat']['id'], "¯\\_(ツ)_/¯" + additional_args)


class MagicCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/magic"
        self.description = "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)")


class TableFlipCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/tableflip"
        self.description = "(╯°□°）╯︵ ┻━┻"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "(╯°□°）╯︵ ┻━┻")


class TableResetCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/tablereset"
        self.description = "┬──┬◡ﾉ(° -°ﾉ)"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "┬──┬◡ﾉ(° -°ﾉ)")


class SnipSnipCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/snipsnip"
        self.description = "( ＾◡＾)っ✂╰⋃╯"

    def execute(self, bot, msg, *args, **kwargs):
        # If we have additional arguments obtain them
        additional_args = get_additional_arguments(self)

        bot.sendMessage(msg['chat']['id'], "( ＾◡＾)っ✂╰⋃╯" + additional_args)


class CryCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/cry"
        self.description = "(ಥ﹏ಥ)"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "(ಥ﹏ಥ)")


class BringItCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/bringit"
        self.description = " ̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿ "

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], " ̿ ̿ ̿'̿'\̵͇̿̿\з=(•_•)=ε/̵͇̿̿/'̿'̿ ̿ ")


class HanzeCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = [
            "/hanze",
            "/harkema",
        ]
        self.description = "凸(-_-)凸"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "凸(-_-)凸")


class AfstuderenCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/afstuderen"
        self.description = "Displays a beautiful song with loads of emotions!"

    def execute(self, bot, msg, *args, **kwargs):
        # If we have additional arguments obtain them
        additional_args = get_additional_arguments(self)

        bot.sendMessage(msg['chat']['id'], "https://youtu.be/bPxxuGaqIjc " + additional_args)


class FuckYouCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/fuckyou"
        self.description = "Returns a 'fuckyou' gif."

    def execute(self, bot, msg, *args, **kwargs):
        fuckyou_gif = open('images/fuckyou.gif', 'rb')
        bot.sendDocument(msg['chat']['id'], fuckyou_gif)


class XkcdLatestCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/xlatest"
        self.description = "Returns the latest xkcd comic!"

    def execute(self, bot, msg, *args, **kwargs):
        xkcd = requests.get("http://xkcd.com/info.0.json").json()

        bot.sendMessage(msg['chat']['id'], '' + str(xkcd['num']) + ' - ' + xkcd['title'] + '\n' +
                        xkcd['img'] + '\n' + xkcd['alt'])


class XkcdRandomCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/xrandom"
        self.description = "Returns a random xkcd comic!"

    def execute(self, bot, msg, *args, **kwargs):
        latest = requests.get("http://xkcd.com/info.0.json").json()
        random_number = randint(1, latest['num'])
        xkcd = requests.get("http://xkcd.com/{}/info.0.json".format(random_number)).json()

        bot.sendMessage(msg['chat']['id'], '' + str(xkcd['num']) + ' - ' + xkcd['title'] + '\n' +
                        xkcd['img'] + '\n' + xkcd['alt'])


class XkcdByIDCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/x"
        self.description = "Returns a xkcd comic for the given command (/x <id>)!"

    def execute(self, bot, msg, *args, **kwargs):
        additional_args = get_additional_arguments(self)
        xkcd = requests.get("http://xkcd.com/{}/info.0.json".format(additional_args)).json()

        bot.sendMessage(msg['chat']['id'], '' + str(xkcd['num']) + ' - ' + xkcd['title'] + '\n' +
                        xkcd['img'] + '\n' + xkcd['alt'])


class SpamCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/spam"
        self.description = "Usage: /spam <amount> <value to spam>"

    def execute(self, bot, msg, *args, **kwargs):
        additional_args = get_additional_arguments(self).split(' ')  # Get the args as list

        if len(additional_args) >= 2:  # Make sure we have the arguments we want to use otherwise return a empty message
            amount = int(additional_args[0])
            value = ' '.join(additional_args[1:])

            for x in range(0, amount):
                bot.sendMessage(msg['chat']['id'], value)

        else:
            bot.sendMessage(msg['chat']['id'], "Missing parameters for the spam command :( please RTFM!")


def get_additional_arguments(obj):
    """
    This method requires an object and will then check if this object has additional arguments.
    If this is the case it will parse those additional arguments and then return it as a string
    """
    args = ''

    try:
        # If the object has arguments parse them to a string and replace the values from the lookup table
        if obj.args:
            # Parse the list to a string
            args = ' '.join(obj.args)

            # Replace the items in the string with entries from the lookup table
            for k, v in config.lookup_table:
                args = args.replace(k, v)

            # Reset the args in the object to reset its state
            obj.args = None
    except AttributeError:
        # No additional args present so we can just skip the parsing
        pass

    return args


##############################################################
### THE FOLLOWING PART MUST STAY AT THE BOTTOM OF THE FILE ###
### THIS IS DUE TO THE WAY PYTHON LOADS THE FILES          ###
##############################################################

# A list containing all the commands as string
command_strings = command_strings = [cls.__name__ for cls in vars()['Command'].__subclasses__()]


class CommandLoader(object):
    """
    This method loads all the commands that subclass the Command object
    After this is done a list with all the command objects will be returned
    """

    def load_commands(self):
        commands = []

        for command in command_strings:
            commands.append(self.__str_to_class(command)())

        # Order all the commands into alphabetical order when saving them in the list and then return the commands
        return sorted(commands, key=lambda x: str(x.get_sorting_key()), reverse=False)

    """
    This method converts a string to a class object
    """

    def __str_to_class(self, str):
        return getattr(sys.modules[__name__], str)
