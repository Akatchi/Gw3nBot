import sys


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
        bot.sendMessage(msg['chat']['id'], "¯\\_(ツ)_/¯")


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
        bot.sendMessage(msg['chat']['id'], "( ＾◡＾)っ✂╰⋃╯")


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

        return commands

    """
    This method converts a string to a class object
    """
    def __str_to_class(self, str):
        return getattr(sys.modules[__name__], str)