import sqlite3
import telebot
from telebot import types


token = '5813076949:AAFi0kUb8uA_N-NIhGaIsKEdOmyWZqoQono'
bot = telebot.TeleBot(token)

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
    bot.send_message(message.chat.id, text=f"Доброго времени суток, {message.from_user.first_name}! Хочется сладенького?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Зарегистрироваться"):
        bot.send_message(message.chat.id, text="Привеет.. Введи свое имя и электронную почту!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Сколько стоят ваши торты?")
        btn2 = types.KeyboardButton("Как быстро я получу заказ?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back, row_width=1)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! Ваше имя добавлено в базу данных!')

        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username

        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)



bot.polling(none_stop=True)