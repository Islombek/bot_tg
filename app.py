# Start the project of telegram bot

from cgitb import text
from markupsafe import Markup
import telebot 
from telebot import types

token = '5336900919:AAHLqiFL8O7UGjuIxpnTSaeHoas8pHTFXaE'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    if item1.text == "Кнопка":
        bot.send_message(message.chat.id, "Вы выбрали кнопку")
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)


@bot.message_handler(content_types="text")
def message_reply(message):
    if message.text == "Кнопка":
        bot.send_message(message.chat.id, "Вы выбрали кнопку")
    


bot.infinity_polling()

