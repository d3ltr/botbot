import telebot

bot = telebot.TeleBot('8236065991:AAEJr-co94Sw6g2QFmnyGFyKMd0XzFaFxSE')


@bot.message_handler(commands=['start'])
def send_start_message(message):
    number = bot.send_message(message.chat.id, 'Напишите 1 или 2')
    bot.register_next_step_handler(number, send_message)



@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == '1':
        message = bot.send_message(message.chat.id, 'Введите число для возведения')
        bot.register_next_step_handler(message, get_square)
    elif message.text == '2':
        message = bot.send_message(message.chat.id, 'Введите число для возведения и умножения')
        bot.register_next_step_handler(message, get_square_n_five)
    else:
        message = bot.send_message(message.chat.id, 'Неверно, напишите 1 или 2')
        bot.register_next_step_handler(message, send_message)


@bot.message_handler(content_types=['text'])
def get_square(number):
    bot.send_message(number.chat.id, int(number.text)**2)

@bot.message_handler(content_types=['text'])
def get_square_n_five(number):
    bot.send_message(number.chat.id, int(number.text)**2 * 5)



bot.polling(non_stop= True)