import telebot
from django_bot.settings import TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def cmd_start(message):
    return bot.reply_to(message, 'Hello, I\'m bot!')
    