import telebot

token = ''
bot = telebot.TeleBot(token, threaded=False)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text='Привет')

@bot.message_handler(content_types=['text'])
def random_message(message):
    bot.send_message(message.chat.id, text=message.text)


bot.polling(none_stop=True)
