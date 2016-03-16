import os
from commands import CommandLoader

BOT_NAME = "@" + os.environ.get('BOTNAME')  # The botname (including the @!)
commands = CommandLoader().load_commands()  # All the commands the bot can use
lookup_table = [
    ('yi', '@Minkey27'),
    ('wahid', '@wahidnory'),
    ('wesley', '@Mavee'),
    ('dirk', '@djdirk'),
    ('vasco', '@Akatchi')
]