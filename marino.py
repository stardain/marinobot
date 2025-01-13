# че должно быть у бота:
# 1. бд
# 2. хэндлеры сообщений
# 3. обработка базовых исключений
# 4. логирование уникальных исключений + сообщение пользователю 
# 5. сервер (через вебхук, щас пока поллинг)

pip install -r requirements.txt

import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = 7242178335:AAFbSlGX-cqoI_1Bgv0Omo5_viR0OEmin2M
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot) # принимает все апдейты от пользователя и обрабатывает их

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    await message.answer("Привет, сладкая попка!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
