from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
import os


load_dotenv('.env')

bot = Bot()
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def android(message:types.Message):
    await message.answer('Hello world')
 
executor.start_polling(dp)