import telebot

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Для того, чтобы я мог сохранить твои данные, напиши мне свое имя.")

@bot.message_handler(func=lambda message: True)
def get_age(message):
    name = message.text
    bot.reply_to(message, "Отлично, теперь напиши свой возраст.")

@bot.message_handler(func=lambda message: True)
def get_address(message):
    age = message.text
    bot.reply_to(message, "Спасибо, теперь напиши свой адрес.")

@bot.message_handler(func=lambda message: True)
def save_data(message):
    address = message.text
    bot.send_message(-964627083, "Пользователь " + 'name' + " отправил свои данные:\nИмя: " + 'name' + "\nВозраст: " + 'age' + "\nАдрес: " + address)

bot.polling()