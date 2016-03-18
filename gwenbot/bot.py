import os
import time
import telepot
import logging

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

        rnd = msg['from']
        if rnd['username'] == 'Minkey27':
            bot.sendMessage(msg['chat']['id'],
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "Sorry Yi :( How about this spam command :D :D :D :D :D :D @Minkey27 :D :D :D @Minkey27"
                                "We will regret this i guess :("
                            )
        else:

            # Get the given command for the received message
            command = CommandFactory.get_command(msg['text'])

            if command is not None:
                command.execute(bot, msg)

            # TODO if we could not find a command model try a lookup in the database to retrieve the command


bot = TelegramBot(os.environ.get('TOKEN'))
bot.notifyOnMessage()

# Configure the logging:
logging.basicConfig(filename='bot.log',level=logging.INFO)

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)