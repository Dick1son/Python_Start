# import telebot

# import random

# from telebot import types

# API_TOKEN='5981118835:AAGW5ddTbc6FFHzlCsnih34Jk7h3SSMo6tE'

# bot = telebot.TeleBot(API_TOKEN)
















# import telebot

# API_TOKEN='5981118835:AAGW5ddTbc6FFHzlCsnih34Jk7h3SSMo6tE'

# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands = ['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Привет, я бот для игры в крестики-нолики.\nПредлагаю ознакомиться с моим функционалом /help")

# @bot.message_handler(commands = ['help'])
# def help_message(message):
#     bot.send_message(message.chat.id, "/play - Начать игру.\n/")

# @bot.message_handler(commands = ['play'])
# def play_reply(message):
#     user_side = 'X'
#     bot.send_message(message.chat.id, "Вы играете за {}".format(user_side))


# bot.polling()