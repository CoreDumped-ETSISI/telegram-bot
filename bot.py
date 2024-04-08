import telebot
from telebot.types import *
from constants import TOKEN

bot = telebot.TeleBot(TOKEN)
#url = 'https://openapi.emtmadrid.es/v1/hello/'
#data = requests.get(url)


#Responde al comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Eyy, bienvenido al bot personal de Core")

@bot.message_handler(commands=['ayuda'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    boton_1 = InlineKeyboardButton("Comandos", url = "")
    boton_2 = InlineKeyboardButton("Contacto", url =  "")
    markup.add(boton_1,boton_2)
    bot.reply_to(message, "Con que necesitas ayuda, pequeña?", reply_markup=markup)



#Responde a un mensaje que no es un comando
@bot.message_handler(content_types=["text"])
def mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, 'Comando *NO* disponible', parse_mode="MarkdownV2")
    else:
        bot.send_message(message.chat.id, "Desea usar alguna función?")
        #Boton para q elija si o o no y q le apareza todos los comandos/funcionalidades que tenga el bot.

# EMT
@bot.message_handler(commands=['bus'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


#Main
if __name__ == '__main__':
    print('Iniciando el bot')

    bot.infinity_polling()
    print('fin')