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


class HeyCommand(Command):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)

        self.query = "/hey"
        self.description = "A simple command to greet people!"

    def execute(self, bot, msg, *args, **kwargs):
        bot.sendMessage(msg['chat']['id'], "Heythere!!!")
