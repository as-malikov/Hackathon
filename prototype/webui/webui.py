#!/usr/bin/python3
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher(bot)

'''
@dp.message_handler(commands=["start"])
async def start(message: Message):

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.reply(message.text)
'''


def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    # создаем webappinfo - формат хранения url
    webAppTest = types.WebAppInfo("https://telegram.mihailgok.ru")
    # создаем кнопку типа webapp
    one_butt = types.KeyboardButton(text="Тестовая страница",
                                    web_app=webAppTest)
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру

    return keyboard  # возвращаем клавиатуру


bot.send_message(message.chat.id,
                 'Привет, я бот для проверки телеграмм webapps!)',
                 reply_markup=webAppKeyboard())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
