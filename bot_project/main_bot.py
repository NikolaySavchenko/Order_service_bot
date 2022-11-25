import os
import sqlite3
import telebot
from telebot import types

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bot_project.settings')
django.setup()
from bot_app.models import Client, Level, Berry, Courier, Decor, Delivery, Form, Order, Topping, Cake

# Для проверки, что есть доступ к базе
levels = Level.objects.all().values()
print(levels[1].get('price'))


oleg_token = '5945463620:AAGnF8c_DSNkx60EzEqI2riWeqVMA0gecDg'

# token = '5813076949:AAFi0kUb8uA_N-NIhGaIsKEdOmyWZqoQono'
bot = telebot.TeleBot(oleg_token)

conn = sqlite3.connect('db.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    conn.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Зарегистрироваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text=f"Доброго времени суток, {message.from_user.first_name}! "
                                           f"Хочется сладенького?", reply_markup=markup)

    user, created = Client.objects.get_or_create(name=message.from_user.first_name)
    print(user)
    print(created)


# @bot.message_handler(content_types=['text'])
# def func(message):
#     if message.text == "👋 Зарегистрироваться":
#         bot.send_message(message.chat.id, text="Привеет.. Введи свое имя и электронную почту!)")
#     elif message.text == "❓ Задать вопрос":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Сколько стоят ваши торты?")
#         btn2 = types.KeyboardButton("Как быстро я получу заказ?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back, row_width=1)
#         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button1 = telebot.types.InlineKeyboardButton(text="Кнопка1", callback_data="button1")
    button2 = telebot.types.InlineKeyboardButton(text="Кнопка2", callback_data="button2")
    keyboard.row(button1, button2)
    bot.send_message(message.from_user.id, "Привет!",  reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_function1(callback_obj):
    if callback_obj.data == "button1":
        bot.send_message(callback_obj.from_user.id, "Вы нажали 🤡 на кнопку 1")
    else:
        bot.send_message(callback_obj.from_user.id, "Вы нажали 🤡 на кнопку 🤖 2")
    bot.answer_callback_query(callback_query_id=callback_obj.id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет 🤡':
        bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных! ')

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)


bot.polling(none_stop=True)