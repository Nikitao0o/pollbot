import telebot as tg
from telebot import types
from buttons_control import But

tinkoff = dict()

cod_txt = open(file="codes.txt",mode="r")
cod = cod_txt.readlines()
for strit in cod:
    tinkoff[strit.split(" : ")[0]] = strit.split(" : ")[1]

class Handlers:
    def __init__(self,bot_main,command = None,content_types = None,content = None, answer = None):
        self.command = command
        self.content_types = content_types
        self.answer = answer
        self.bot_main = bot_main
        self.content = content
    def message(self):
        @self.bot_main.message_handler(commands=self.command,content_types=self.content_types)
        def request_message(message):
            if message.text == self.content or self.content == None:
                self.bot_main.send_message(message.chat.id,text=self.answer)
#            But.build_but(self.command)
            with open(file="info.txt",mode="+a") as fb:
                fr = fb.readlines()
                if not(ids := (message.chat.id) in fr):
                    fb.write(f"{ids} \n")
