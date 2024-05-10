import telebot as tg
from telebot import types


class Handlers:
    def __init__(self,bot_main,command = None,content = None, answer = None):
        self.command = command
        self.content = content
        self.answer = answer
        self.bot_main = bot_main
    def hand(self):
        @self.bot_main.message_handler(commands=self.command,content_types=self.content)
        def request_message(message):
            self.bot_main.send_message(message.chat.id,text=self.answer)
