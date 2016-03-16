from config import BOT_NAME, commands


class CommandFactory(object):
    @staticmethod
    def get_command(query):
        query = CommandFactory.format_query(query)

        # Get all the additional argument from the query (if present)
        # args will contain a list of lowercased additional arguments
        args = query.split(' ')

        # If there are additional arguments present we have to set the query with the first
        # entry from the list (otherwise its a multipart string for example: "/hey how are you doing" which
        # Wont return a hit with the command.get_query() method.
        if args:
            query = args[0]
            args.remove(args[0])

        # Get the command that corresponds with the given query (if present)
        for command in commands:
            if query in command.get_query():
                # If there are additional arguments pass them to the command object
                if args:
                    command.args = args

                return command

    """
    Sometimes the query contains the botname (for example: /help@BotName)
    This method will remove the botname from the query and then returns the
    `cleaned` query
    """
    @staticmethod
    def format_query(query):
        query = query.lower()  # lowercase the query to make the comparison easier
        lower_bot_name = BOT_NAME.lower()  # Same for the BOT_NAME

        if query.endswith(lower_bot_name):
            query = query.replace(lower_bot_name, "")

        return query
