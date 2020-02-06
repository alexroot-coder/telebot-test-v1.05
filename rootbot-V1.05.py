# -*- coding: utf-8 -*-
import telebot
import parse
import datetime
import time
import weather as w
import news as n
import config as con
import random
from telebot import types

for_rand_0=0
for_rand_1000000=1000000

bot = telebot.TeleBot(con.TOKEN) #TOKEN

#msg = str(parse.title)
user = bot.get_me()
#start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start \nТеперь напиши /help')
#help 
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,'Вот небольшой список команд,которые я могу выполнить:\n/date - Дата и время\n/news - Последние новости\n/geo - Геолокация\nПогода - просто напиши мне слово "Погода"' + '\n'+ '/rand - Рандомное число от 0 до 1000000')
#date 
@bot.message_handler(commands=['date'])
def date_message(message):
    bot.send_message(message.chat.id,'Дата: '+str(date()))
    clear(date)
#news 
@bot.message_handler(commands=['news'])
def news_message(message):
    bot.send_message(message.chat.id,str(last_news()))
    last_news_clear(last_news)
#geo
@bot.message_handler(commands=["geo"])
def geo_message(message):
    keyboard = types.ReplyKeyboardMarkup(True,True) #row_width=1, resize_keyboard=True
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Нажми на кнопку и передай мне свое местоположение", reply_markup=keyboard)

@bot.message_handler(content_types=["location"])
def location(message):
	bot.send_location(message.chat.id, latitude, longitude)
#different text
@bot.message_handler(content_types=['text'])	
def sent_text(message):
	if message.text.lower() == 'погода':
		bot.send_message(message.chat.id, str(weather1()))
		clear_weather(weather1)
	elif message.text.lower() == 'пока':
		bot.send_message(message.chat.id,'Прощай😕')
	elif message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет😁')
	elif message.text == '/rand':
		bot.send_message(message.chat.id,randd(a=for_rand_0,b=for_rand_1000000))
	elif message.text == 'spam':
		bot.send_message(message.chat.id,'Рассылка вкл')
		global spam
		spam = True
		while spam:
			bot.send_message(message.chat.id,last_news())
			last_news_clear(last_news)
			time.sleep(28000)
	elif message.text == 'stop':
		spam = False
		bot.send_message(message.chat.id,'Рассылка выкл')
	else:
		bot.send_message(message.chat.id, 'Я еще не всё понимаю🤨')
	#print(message.from_user.username,message.text)
#sticker	
@bot.message_handler(content_types=['sticker'])
def sent_stick(message):
	bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAOPXjW-xLLIM-SU0pV7tWs3wMM5l24AAh4AA5z-MjDaa3SCaHx-bBgE')

def randd(a,b):
	val = random.randint(a,b)
	return val

def date():
	date = str(datetime.date.today()) + '\n' +str(datetime.datetime.now().time().hour) + ':' + str(datetime.datetime.now().time().minute) + ':' + str(datetime.datetime.now().time().second)
	return date

def clear(date):
	date = None
	return date

def weather1():
	weather1 = (str(w.info) +','+ str(w.info2) +'\n' +str(date())+'\n' + 'Температура: ' + str(w.a1) + '°C' + '\n' + 'Минимальная температура: ' + str(w.a2) + '°C' + '\n' + 'Максимальная температура: ' + str(w.a3) + '°C' + '\n' + 'Погодные условия: ' + str(w.a0)+ '\n' + 'Ветер: ' + str(w.a4)+' м/с')
	return weather1

def clear_weather(weather1):
	weather1 = None
	return weather1

def last_news():
	last_news = ('Последние новости: '+ str(n.b0)+ '\n' + str(n.b1)+ '\n' + str(n.b2))
	return last_news

def last_news_clear(last_news):
	last_news = None
	return last_news

#bot.polling(none_stop=True)
if __name__ == '__main__':
     bot.infinity_polling()


