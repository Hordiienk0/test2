import telebot
import random
import glob
import os
from telebot import types


path = r'C:\Users\Gigabyte\Desktop\bot\photos'

bot = telebot.TeleBot('1116253924:AAF13mSOZsJspMR_c8WtXFBUqwMVWkRnqvU')

@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("I want hentai")
    markup.add(item1)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>,".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def send_rand_photo(message):
    if message.text == 'I want hentai':

        all_photo_in_directory=os.listdir(path)
        random_photo=random.choice(all_photo_in_directory)
        img=open(path + '/' +random_photo, 'rb')
        bot.send_chat_action(message.from_user.id,'upload_photo')
        bot.send_photo(message.from_user.id,img)
        img.close()
bot.polling(none_stop=False)