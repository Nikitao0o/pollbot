import telebot as tg
from telebot import types
from controller import Handlers

token = "6942992841:AAHVi3tA-RrTSrkAxw-72OOoYhmc_KCR8fQ"
bot_main = tg.TeleBot(token)

Handlers(command=["start"],answer="Работаю",bot_main=bot_main).hand()


bot_main.polling(non_stop=True)

