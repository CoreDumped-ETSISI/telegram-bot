import telebot
from constants import TOKEN
import time
import _thread

bot = telebot.TeleBot(TOKEN)


#Responde al comando /start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


#Responde a un mensaje que no es un comando
@bot.message_handler(content_types=["text"])
def mensajes_texto(message):
    if message.text.startswith("/"):

        bot.send_message(message.chat.id, 'Comando *NO* disponible', parse_mode="MarkdownV2")
    else:
        bot.send_message(message.chat.id, "Desea usar alguna función?")
        #Boton para q elija si o o no y q le apareza todos los comandos/funcionalidades que tenga el bot.







#Main
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('fin')



