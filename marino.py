"""
че должно быть у бота:
# 1. бд
# 2. хэндлеры сообщений
# 3. обработка базовых исключений
# 4. логирование уникальных исключений + сообщение пользователю 
# 5. сервер (через вебхук как-то)
"""

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7242178335:AAFbSlGX-cqoI_1Bgv0Omo5_viR0OEmin2M'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher() # принимает все апдейты от пользователя и обрабатывает их

@dp.message(Command("start"))
async def message_handler(message: types.Message):
    """
    greets a ho
    """
    await message.answer("hello ho <3")

@dp.message()
async def echo_message(message: types.Message):
    """
    mocks them
    """
    await message.answer(f"hahahah, {message.text}")

if __name__ == '__main__':
    Dispatcher.start_polling(dp, skip_updates=True)

# git remote add origin https://github.com/stardain/marinobot.git