import telebot

bot = telebot.TeleBot("1016441239:AAF42LkLUVRBbvvyFG5XgiBD567R-y2rfik")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
