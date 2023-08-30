############################
# ________________________ #
# -------Developer---------#
# --Alexander Solyanskiy-- #
# --------[NORM1K]---------#
# _________________________#
############################

import telebot
from telebot import types
import os
import random


bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    mess = f'Привет, <b>{message.from_user.first_name}</b> приятно познакомиться я Багун.\nНапиши /button'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('Плейлист🎶')
    start = types.KeyboardButton('Получить фото📷')
    help = types.KeyboardButton('Помощь💬')
    bio = types.KeyboardButton('Биография📓')
    off = types.KeyboardButton('Деактивировать клавиатуру❌')
    markup.add(website, start, help, bio, off)
    bot.send_message(message.chat.id, 'Клавиатура активирована✅', reply_markup=markup)


@bot.message_handler(commands=['music'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Плейлист', url="https://clikny.ru/ujnoY"))
    bot.send_message(message.chat.id, 'Перейти по ссылке', reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "Хохохо":
        bot.send_message(message.chat.id, "Я люблю ебланить", parse_mode='html')
    elif message.text == "Багун":
        bot.send_message(message.chat.id, "Я не хочу быть капитаном по охране труда!!", parse_mode='html')
    if message.text == "Багун ты где?":
        bot.send_message(message.chat.id, "Я на курилке", parse_mode='html')
    elif message.text == "Иди нахуй":
        bot.send_message(message.chat.id, "Сам иди нахуй не обзывайся", parse_mode='html')
    if message.text == "Плейлист🎶":
        bot.send_message(message.chat.id, "Вот ссылка на плейлист: https://clikny.ru/ujnoY", parse_mode='html')
    elif message.text == "Получить фото📷":
        photo = open('test/' + random.choice(os.listdir('test')), 'rb')
        bot.send_photo(message.chat.id, photo, caption='Вот твоя фотка')
    if message.text == "Багун где зая?":
        bot.send_message(message.chat.id, "В огороде роется, сказала что морковку ищет", parse_mode='html')
    elif message.text == "Минск":
        bot.send_message(message.chat.id, "Красный", parse_mode='html')
    if message.text == "Помощь💬":
        bot.send_message(message.chat.id, "Список фраз на данный момент:\n1. Хохохо\n"
                                          "2. Багун\n3. Багун ты где?\n4. Иди нахуй\n5. Получить фото\n"
                                          "6. Багун где зая?\n7. Минск\n_____________________________\n"
                                          "Список команд:\n/button - Активация клавиатуры\n/music - Получить ссылку "
                                          "на плейлист\n/start - Получить приветствие от бота.", parse_mode='html')
    elif message.text == "Биография📓":
        bot.send_message(message.chat.id, "Владислав Багун, 18 лет, курит Минск Красный,Фест,Премьер.\n"
                                          "Все называют его гоблином либо вурдалаком, обижается на пустоту,\n"
                                          "Попиздился с Голиком на по в начале года, горбатый блять как знак вопроса,\n"
                                          "Уши как у мыши.")
    if message.text == "Деактивировать клавиатуру❌":
        bot.send_message(message.chat.id, 'Клавиатура деактивирована❌.\nЧтобы активировать нажмите на\n'
                                          '[/button]', reply_markup=types.ReplyKeyboardRemove())
    elif message.text == "Столица Беларуси?":
        bot.send_message(message.chat.id, 'Не знаю это слишком сложный вопрос🤬')

    rock = ['Камень', 'Ножницы', 'Бумага']
    if message.text == "Камень":
        bot.send_message(message.chat.id, random.choice(rock))
    if message.text == "Ножницы":
        bot.send_message(message.chat.id, random.choice(rock))
    if message.text == "Бумага":
        bot.send_message(message.chat.id, random.choice(rock))


bot.polling(none_stop=True)
