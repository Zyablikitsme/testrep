import telebot
import random

bot = telebot.TeleBot("1016441239:AAF42LkLUVRBbvvyFG5XgiBD567R-y2rfik")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(commands=['random'])
def randome(message):
    bot.reply_to(message, str(random.randint(1,100)))

bot.polling(none_stop=True)

