import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

import strings as st

def load():
    with open(st.JSON_PATH, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
    return BD_local

def get_token():
    token = ''
    with open(st.TOKEN_PATH, 'r', encoding='utf-8') as file:
        token = file.read()
    
    return token

def get_keyboard(callBackData, len_of_keyboard , url):
    keyboard = []
    for i in range(len_of_keyboard):
        keyboard.append([] * len_of_keyboard)
    for i in range(2):
        keyboard[i].append(InlineKeyboardButton(callBackData[i],url=url[i] , callback_data=callBackData[i]))

    return keyboard

def get_keyboard1(callBackData, len_of_keyboard):
    keyboard = []
    for i in range(len_of_keyboard):
        keyboard.append([] * len_of_keyboard)
    for i in range(2):
        keyboard[i].append(InlineKeyboardButton(callBackData[i], callback_data=callBackData[i]))

    return keyboard

def get_keyboard2(callBackData):
    keyboard = [[], []]
    for i in range(len(keyboard)):
        keyboard[i].append(InlineKeyboardButton(callBackData[i], callback_data=callBackData[i]))

    return keyboard

def button(update, _):
    BD = load()
    format_data = ""
    data = []
    url = []
    query = update.callback_query
    callbackData = query.data
    selected_company = query.data
    callbackData = BD.get(callbackData)
    for x in range(len(callbackData)):
        for y, k in callbackData[x].items():
            if y == "url":
                url.append(k)
                continue
            format_data += k
            format_data += ' '
        data.append(format_data)
        format_data = ""
    
    query.edit_message_text(text=st.ANSW_CHOICE_PHONE_MODEL + selected_company,reply_markup=InlineKeyboardMarkup(get_keyboard(data, len(data), url)))

def start_command(update, _):
    update.message.reply_text(st.ANSW_START)

def help_command(update, _):
    update.message.reply_text(st.ANSW_HELP)

def exception_command(update, _):
    update.message.reply_text(st.ANSW_EXCEPTION)

def view_command(update, _):
    data = []
    BD = load()
    for x in BD.keys():
        data.append(x)
    update.message.reply_text(st.ANSW_CHOICE_COMPANY, reply_markup=InlineKeyboardMarkup(get_keyboard1(data, len(data))))

def add_command(update, _):
    
    update.message.reply_text(st.ANSW_ADD)
    



if __name__ == '__main__':
    updater = Updater(get_token())

    updater.dispatcher.add_handler(CommandHandler('start', start_command))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('view', view_command))
    updater.dispatcher.add_handler(CommandHandler('add', add_command))
    # updater.dispatcher.add_handler(CommandHandler('edit', edit_command))
    # updater.dispatcher.add_handler(CommandHandler('delete', del_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, exception_command))
    updater.dispatcher.add_handler(CallbackQueryHandler(button)) 
    

    # Запуск бота
    updater.start_polling()
    updater.idle()