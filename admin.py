#!/usr/bin/python3


from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery, \
     InlineKeyboardMarkup, InlineKeyboardButton

from config import API_TOKEN
from object.Object import Object
from gateway import add_object

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
obj = Object(0, 0, 0, 0, 0, 0, 0)


def create_button(button_name, button_callback):
    return InlineKeyboardButton(text=button_name,
                                callback_data=button_callback)


keyboard_adm_mode = InlineKeyboardMarkup()
keyboard_adm_mode.add(create_button('Добавить объект', 'adm-add_object'))
keyboard_adm_mode.add(create_button('Удалить объект', 'adm-delete_object'))
keyboard_adm_mode.add(create_button('Изменить объект', 'adm-edit_objetct'))
keyboard_adm_mode.add(create_button('Return User Mode', 'adm-user_mode'))


async def change_mode(callback: CallbackQuery, keyboard_adm):
    keyboard_adm = keyboard_adm_mode
    await callback.message.edit_text(text="Что ты хочешь изменить?",
                                     reply_markup=keyboard_adm)


@dp.callback_query_handler()
async def adm_menu(callback: CallbackQuery, keyboard_adm):
    if callback.data[4:] == 'change_mode':
        await change_mode(callback, keyboard_adm)
    elif callback.data[4:] == 'add_object':
        await command_add_object(callback)
    elif callback.data[4:] == 'delete_object':
        print("DELETE OBJECT")
    elif callback.data[4:] == 'edit_objetct':
        print("EDIT OBJECT")
    elif callback.data[4:] == 'user_mode':
        await callback.message.answer("Что ты хочешь забронировать?",
                                      reply_markup=keyboard_adm_mode)
    else:
        await callback.answer(text='neen')


async def command_add_object(callback: CallbackQuery):
    print("ADD OBJECT")


async def cmd_cancel(message: Message):
    await message.answer("Действие отменено",
                         reply_markup=types.ReplyKeyboardRemove())


async def secret_command(message: types.Message):
    await message.answer("Команда доступна только разработчику.")
