# telebot  =>  pip install pytelegrambotapi

import telebot 

from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot("8809466266:AAGRfkX8dpRDiu88fqH1zAHmOddJehNcmXA")

@bot.message_handler(commands=["start"])
def boshlash_f(message):
    bot.send_message(message.chat.id, text= "Salom bu mening 1chi btns kodim!!!")

bot.message_handler(commands=['text'])
def send_f(message):
    guruh = ReplyKeyboardMarkup(resize_keyboard=True)
    tugma = KeyboardButton(text='soat')
    tugma2 = KeyboardButton(text='time')
    guruh.add(tugma, tugma2)


    bot.send_message(message.chat.id, text='text botimizga xush kelibsiz!!',reply_markup=guruh)


bot.message_handler(content_types='text')
def all_msg(message):
    matn = message.text

    if 'salom' in matn or 'hello' in matn:
        bot.send.message(message.chat.id, text='Assalomu Aleykum')
    elif 'soat' in matn:
        bot.send_message(message.chat.id, text="soat: 17:17")
            

print("working...")
bot.infinity_polling()