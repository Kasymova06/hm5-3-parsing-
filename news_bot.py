from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import os, logging, requests

load_dotenv('.env')

bot = Bot(os.environ.get('token'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет это бот новостей")

@dp.message_handler(commands = 'news')
async def get_news(message:types.Message):
    url = "https://akipress.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='newslink')
    n = 0
    for news in quotes:
        n += 1
        link = news.get('href')
        print(link)
        with open('parsing.txt', 'a+', encoding="utf-8") as file:
            file.write(f"{n}) {news.text}\n")
            await message.answer(f"{n}) {news.text}\n  Источник:{link}")

executor.start_polling(dp)