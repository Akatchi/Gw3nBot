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

# Blacklisted users who are forbidden from sending messages (usernames without @)
blacklisted_usernames = [
    'Minkey27',
    'Mavee',
    'Akatchi',
]
blacklisted_message = "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "Sorry mister :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27" \
    "We will regret this i guess :("