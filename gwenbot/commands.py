class Command(object):
    """
    The constructor of the command object.
    """
    def __init__(self, query=None, description=None):
        self.query = query
        self.description = description

    """
    The query is the keyword that triggers the command (for example /help)
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
        bot.sendMessage(msg['chat']['id'], self.description)


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