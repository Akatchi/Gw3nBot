import os
import time
import telepot

from factory import CommandFactory


class TelegramBot(telepot.Bot):
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        # Sometimes the content_type is not text.
        # The bot can (at the moment) only process text messages
        if not content_type == 'text':
            raise NotImplementedError

        # Get the given command for the received message
        command = CommandFactory.get_command(msg['text'])

        if command is not None:
            command.execute(bot, msg)

        # TODO if we could not find a command model try a lookup in the database to retrieve the command


bot = TelegramBot(os.environ.get('TOKEN'))
bot.notifyOnMessage()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)