import telebot
import config
import random

from telebot import types


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("МТУСИ")
    item2=types.KeyboardButton("/help")
    item3=types.KeyboardButton("/stik")
    item4=types.KeyboardButton("/kotiki")

    markup.add(item1,item2,item3,item4)

    bot.send_message(message.chat.id, "Привет! Этот бот попытается помочь тебе 😼🤍. Если хочешь побольше узнать обо мне, напиши: /help".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def kb(message):
    if message.chat.type == 'private':
        if message.text == 'МТУСИ':
            bot.send_message(message.chat.id,'Хорошо) Воть😊:https://mtuci.ru/')
        if message.text == '/stik':
                bot.send_message(message.chat.id, 'Хорошо) Воть стики😊: https://t.me/addstickers/plisssa')
        if message.text == '/kotiki':
                bot.send_message(message.chat.id, 'Хорошо) Воть классные стики с котиками😊: https://t.me/addstickers/KLDCAT')
                bot.send_message(message.chat.id, 'Воть ещё) https://t.me/addstickers/Cats_ker4gen_by_fStikBot')
                bot.send_message(message.chat.id, 'А хочешь увидеть самые милые стикеры?) Если да, напиши Хочу 🙃')
        elif message.text == '/help':
            bot.send_message(message.chat.id,'Я тебе отвечу на... Привет, Как дела?, Что делаешь?, Спасибо, Пока.  Если захочешь увидеть мои стикеры - напиши команду /stik. Если хочешь что-нибудь посмотреть пиши /watch. Если захочешь стикеры с котиками напиши /kotiki. Если хочешь случайное число от 0 до 100 то напиши /rand.')
        elif message.text == '/rand':
            bot.send_message(message.chat.id,str(random.randint(0,100)))
        elif message.text == '/rs':
            bot.send_message(message.chat.id,'Хорошо) Воть расписание😊:https://mtuci.ru/time-table/')
        elif message.text == 'Привет':
            bot.send_message(message.chat.id, 'Приветики')
        elif message.text == 'привет':
            bot.send_message(message.chat.id, 'Приветики')
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id,'👍🏻')
        elif message.text == 'Как дела':
            bot.send_message(message.chat.id, 'Всё хорошо 😉')
        elif message.text == 'как дела':
            bot.send_message(message.chat.id, 'Отлично:)')
        elif message.text == 'Хочу':
            bot.send_message(message.chat.id, 'Лови)  https://t.me/addstickers/ka_tyu_ha')
        elif message.text == 'хочу':
            bot.send_message(message.chat.id, 'Лови)  https://t.me/addstickers/ka_tyu_ha')
        elif message.text == 'Спасибо':
            bot.send_message(message.chat.id, '❤️')
        elif message.text == 'спасибо':
            bot.send_message(message.chat.id, '😘')
        elif message.text == 'пока':
            bot.send_message(message.chat.id, '👋')
        elif message.text == '/watch':
            bot.send_message(message.chat.id, 'Хорошо) Воть, здесь точно есть что посмотреть😊:https://www.youtube.com')
        elif message.text == 'Что делаешь?':
            bot.send_message(message.chat.id, 'Чилю')
        elif message.text == 'что делаешь?':
            bot.send_message(message.chat.id, 'Жду твоих команд 😑')
        elif message.text == 'Пока':
            bot.send_message(message.chat.id,'Ну пока(')




# RUN
bot.polling(none_stop=True)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет! Хочешь узнать информацию о МТУСИ?".format(message.from_user,bot.get_me()), parse_mode='html')
