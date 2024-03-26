import telebot
from constants import TOKEN

bot = telebot.TeleBot(TOKEN)


#Responde al comando /start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


#Responde a un mensaje
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


#Main
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('fin')



