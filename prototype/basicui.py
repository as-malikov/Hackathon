#!/usr/bin/python3
import sys
import logging
import datetime
# CI/CD
if len(sys.argv) != 1:
    if sys.argv[1] == 'Success':
        sys.exit()

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, \
     InlineKeyboardMarkup, InlineKeyboardButton
from object.User import User
from object.Schedule import Schedule
from gateway import verify_user, get_object, get_object_by_id, add_schedule
from config import API_TOKEN

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
user = User(0, 0, 0, 0, 0, 0)
only_object = None
only_date = None
date_shedule = None


def create_button(button_name, button_callback):
    return InlineKeyboardButton(text=button_name,
                                callback_data=button_callback)


time_all_day = [str(i)+':00:00' for i in range(0, 24)]
time_end_all_day = [str(i)+':59:59' for i in range(0, 24)]
max_keyboard = 8
keyboard_adm = InlineKeyboardMarkup()
# 0 - booking, 1 - rooms
check_first = [True for _ in range(max_keyboard)]
markup = [InlineKeyboardMarkup() for _ in range(max_keyboard)]
start_button = {'Забронировать': 'booking', 'Обратная связь': 'feedback'}
for name_button, callback_button in start_button.items():
    markup[0].add(create_button(name_button, callback_button))
    keyboard_adm.add(create_button(name_button, callback_button))
keyboard_adm.add(create_button('admin', 'adm'))


@dp.message_handler(commands=["start"])
async def start(message: Message):
    user.telegram_id = message.from_user.id
    await verify_user(user)
    await checker(message)


async def checker(message: Message):
    if user.telegram_id > 0:
        if user.role_id == 2:
            await message.answer("Что ты хочешь забронировать?",
                                 reply_markup=keyboard_adm)
        else:
            await message.answer("Что ты хочешь забронировать?",
                                 reply_markup=markup[0])
    else:
        await message.answer("Введи свой логин\n \
            (в формате '.login')\n(Без \'@student.21-school.ru\')")


@dp.message_handler(lambda message: message.text[0] == '.'
                    if len(message.text) > 1 else False)
async def register_user(message: Message):
    await message.answer('Вы успешно зарегистрированы')
    await checker(message)


@dp.callback_query_handler()
async def booking_menu(callback: CallbackQuery):
    back_list = ['meeting', 'kitchen', 'play_room']
    user._telegram_id = callback.from_user.id
    await verify_user(user)
    if callback.data == 'booking':
        await booking(callback)
    elif callback.data == 'feedback':
        report = 'Отправь обратную связь\n(Одним сообщением)'
        await callback.message.edit_text(text=report)
    elif callback.data[:4] == 'back':
        await back(callback, markup[int(callback.data[-1])])
    elif callback.data in back_list:
        await rooms(callback)
    elif callback.data == 'inventory':
        await inventory(callback)
    elif callback.data == 'hall':
        await hall(callback)
    elif callback.data[:3] == 'day':
        await choose_time_day(callback)
    elif callback.data[:7] == 'timeday':
        await choose_time(callback)
    elif callback.data[:4] == 'time':
        await booking_done(callback)
    else:
        await choose_day(callback)


async def booking_done(callback: CallbackQuery):
    global markup, check_first, only_object, only_date, date_shedule
    print(user.id)
    got_object = await get_object_by_id(only_object)
    arr_i = callback.data.split('-')
    start_date = str(date_shedule) + ' ' + time_all_day[int(arr_i[1])]
    end_date = str(date_shedule) + ' ' + time_end_all_day[int(arr_i[1])]
    shedule_done = Schedule(got_object.id, user.id, start_date, end_date, 1)
    report = f'Вы забронировали {got_object.name}' \
             f'\n на дату {only_date}\n {time_all_day[int(arr_i[1])]}'
    await add_schedule(shedule_done)
    if check_first[7]:
        markup[7].add(create_button('Главное меню', 'back-0'))
        check_first[7] = False
    await callback.message.edit_text(report, reply_markup=markup[7])


async def choose_time(callback: CallbackQuery):
    global time_all_day, only_object
    got_object = await get_object_by_id(only_object)
    about_object = f'{got_object.name}\n Этаж {got_object.floor}' \
                   f'\n{got_object.desc}\n'
    time_keyboard = InlineKeyboardMarkup()
    times = callback.data[8:].split('-')
    start_time = int(times[0])
    end_time = int(times[1])
    print(end_time, type(end_time))
    for i in range(start_time, end_time):
        time_keyboard.add(create_button(time_all_day[i], 'time-' + str(i)))
    time_keyboard.add(create_button('<< Назад', 'back-6'))
    report = about_object+'На какое время ты хочешь забронировать?'
    await callback.message.edit_text(report, reply_markup=time_keyboard)


async def choose_time_day(callback: CallbackQuery):
    global markup, check_first, only_object, only_date, date_shedule
    date_list = callback.data.split('-')
    only_date = date_list[3]+'/'+date_list[2]+'/'+date_list[1]
    date_shedule = date_list[1]+'-'+date_list[2]+'-'+date_list[3]
    got_object = await get_object_by_id(only_object)
    about_object = f'{got_object.name}\n Этаж {got_object.floor}' \
                   f'\n{got_object.desc}\n'
    if check_first[6]:
        time_date = {'0-5': '0-6', '6-11': '6-12', '12-17': '12-18',
                     '18-23': '18-24'}
        for name, call in time_date.items():
            markup[6].add(create_button(name, 'timeday-'+call))
        markup[6].add(create_button('<< Назад', 'back-5'))
        check_first[6] = False
    report = about_object+'На какое время ты хочешь забронировать?'
    await callback.message.edit_text(report, reply_markup=markup[6])


async def choose_day(callback: CallbackQuery):
    global markup, check_first, only_object
    data_obj = callback.data.split('-')
    only_object = data_obj[1]
    keyboar = InlineKeyboardMarkup()
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    day = {'Сегодня': 'day-' + str(today),
           'Завтра': 'day-' + str(tomorrow)}
    for i in range(1, 5):
        week_day = str(today + datetime.timedelta(days=1 + i))
        day[week_day] = 'day-'+week_day
    for name, call in day.items():
        keyboar.add(create_button(name, call))
    keyboar.add(create_button('<< Назад', 'back-'+callback.data[-1]))
    markup[5] = keyboar
    report = 'На какой день хочешь забронировать?'
    await callback.message.edit_text(report, reply_markup=markup[5])


async def hall(callback: CallbackQuery):
    global markup, check_first
    if check_first[3]:
        obj = await get_object(user)
        for button in obj:
            if button.type == 5:
                markup[3].add(create_button(button.name,
                                            'hall-' + str(button.id) + '-3'))
        markup[3].add(create_button('<< Назад', 'back-1'))
        check_first[3] = False
    await callback.message.edit_reply_markup(markup[3])


async def inventory(callback: CallbackQuery):
    global markup, check_first
    if check_first[2]:
        obj = await get_object(user)
        item_id = [2, 3, 7, 8]
        for button in obj:
            if button.type in item_id:
                markup[2].add(create_button(button.name,
                                            'inv-' + str(button.id) + '-2'))
        markup[2].add(create_button('<< Назад', 'back-1'))
        check_first[2] = False
    await callback.message.edit_reply_markup(markup[2])


async def rooms(callback: CallbackQuery):
    global check_first, markup
    keyboars = InlineKeyboardMarkup()
    obj = await get_object(user)
    type_rooms = {'1': 'meeting', '4': 'kitchen', '6': 'play_room'}
    for button in obj:
        if type_rooms.get(str(button.type)) == callback.data:
            keyboars.add(create_button(button.name,
                                       'rooms-' + str(button.id) + '-4'))
    keyboars.add(create_button('<< Назад', 'back-1'))
    markup[4] = keyboars
    await callback.message.edit_reply_markup(markup[4])


async def back(callback: CallbackQuery, keyboard_back):
    global markup
    if callback.data[-1] == 7:
        await callback.message.answer(text='Что ты хочешь забронировать?',
                                      reply_markup=markup[0])
    else:
        if user.role_id == 2 and keyboard_back == 0:
            keyboard_back = keyboard_adm
        await callback.message.edit_reply_markup(keyboard_back)


async def booking(callback: CallbackQuery):
    global check_first, markup
    if check_first[0]:
        obj = await get_object(user)
        type_id = []
        invent_id = [2, 3, 7, 8]
        for button in obj:
            if button.type == 1 and button.type not in type_id:
                markup[1].add(create_button('Переговорки', 'meeting'))
            elif button.type == 4 and button.type not in type_id:
                markup[1].add(create_button('Кухни', 'kitchen'))
            elif button.type == 5 and button.type not in type_id:
                markup[1].add(create_button('Холл / Конференц зал', 'hall'))
            elif button.type == 6 and button.type not in type_id:
                markup[1].add(create_button('Игровые', 'play_room'))
            elif button.type in invent_id and button.type not in type_id:
                markup[1].add(create_button('Инвентарь', 'inventory'))
                for i in invent_id:
                    type_id.append(i)
            type_id.append(button.type)
        markup[1].add(create_button('<< Назад', 'back-0'))
        check_first[0] = False
    await callback.message.edit_reply_markup(markup[1])


@dp.message_handler()
async def feedback_get(message: Message):
    await message.answer(text='Сообщение принято')
    user.telegram_id = message.from_user.id
    await verify_user(user)
    if user.role_id == 2:
        await message.answer(text='Что ты хочешь забронировать?',
                             reply_markup=keyboard_adm)
    else:
        await message.answer(text='Что ты хочешь забронировать?',
                             reply_markup=markup[0])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
