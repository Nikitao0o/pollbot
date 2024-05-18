import telebot as tg
from telebot import types
from controller import Handlers

token = "6942992841:AAHVi3tA-RrTSrkAxw-72OOoYhmc_KCR8fQ"
bot_main = tg.TeleBot(token)

Handlers(command=["start"],answer="Приве-е-е-е-е-т",bot_main=bot_main)
Handlers(content_types=["text"],bot_main=bot_main)




if __name__ == "__name__":
    print("Work") #Не работает

bot_main.polling(non_stop=True)
