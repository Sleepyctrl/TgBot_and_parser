# -*- coding: UTF-8 -*-
#!/usr/bin/env python

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton,Message
from config import TOKEN
import sqlite3

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
query=""

inline_kb1 = InlineKeyboardButton('Create Enemy', callback_data='button1')
button1 = KeyboardButton('CR > 1', callback_data='CR > 1')
button2 = KeyboardButton('CR 1-2')
button3 = KeyboardButton('CR 3-4')
button4 = KeyboardButton('CR 5-6')
button5 = KeyboardButton('CR 7-8')
button6 = KeyboardButton('CR 9-10')
button7 = KeyboardButton('CR 11-12')
button8 = KeyboardButton('CR 13-14')
button9 = KeyboardButton('CR 15-16')
button10 = KeyboardButton('CR 17-18')
button11 = KeyboardButton('CR 19-20')
button12 = KeyboardButton('CR 20+')

#Создание и вывод кнопок в тг боте
markup4 = ReplyKeyboardMarkup(one_time_keyboard=True).row(
    button1, button2, button3, button4, button5, button6
)
markup4.row(button7, button8, button9, button10, button11, button12)


inline_kb1 = InlineKeyboardMarkup().add(inline_kb1)
#стартовое сообщение
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Use button "Create Enemy", to generate a random opponent', reply_markup=inline_kb1)
    
@dp.message_handler(content_types=['text'], text='CR > 1')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR >1' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])
   
@dp.message_handler(content_types=['text'], text='CR 1-2')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 001'or CR_enemy ='CR 002' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 3-4')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 003'or CR_enemy ='CR 004' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 5-6')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 005'or CR_enemy ='CR 006' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 7-8')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 007'or CR_enemy ='CR 008' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 9-10')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 009'or CR_enemy ='CR 010' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 11-12')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 011'or CR_enemy ='CR 012' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 13-14')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 013'or CR_enemy ='CR 014' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 15-16')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 015'or CR_enemy ='CR 016' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 17-18')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 017'or CR_enemy ='CR 018' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 19-20')
async def spam(message: Message):
    query="SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 019'or CR_enemy ='CR 020' ORDER BY RANDOM() LIMIT 1"
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.message_handler(content_types=['text'], text='CR 19-20')
async def spam(message: Message):
    query='''SELECT * FROM Dnd_random_enemies WHERE CR_enemy = 'CR 021'
    or CR_enemy ='CR 022'
    or CR_enemy ='CR 023'
    or CR_enemy ='CR 024'
    or CR_enemy ='CR 025'
    or CR_enemy ='CR 026'
    or CR_enemy ='CR 027'
    or CR_enemy ='CR 028'
    or CR_enemy ='CR 029'
    or CR_enemy ='CR 030'
    or CR_enemy ='CR 035'
    or CR_enemy ='CR 037' ORDER BY RANDOM() LIMIT 1'''
    with sqlite3.connect('Dnd_random_enemies.db') as connection:
            show=connection.cursor().execute(query).fetchone()
    await message.answer(show[1]+'\n'+show[2]+
            '\nDescription: \n'+show[3]+'\n'+show[4])

@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    call = callback_query.data
    if call == 'button1':
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,'Choose your opponent CR',reply_markup=markup4)
    


if __name__ == '__main__':
    executor.start_polling(dp)
