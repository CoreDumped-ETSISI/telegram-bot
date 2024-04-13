import telebot
import requests
from telebot.types import *
from constants import TOKEN, clientId
#passkey
import time

bot = telebot.TeleBot(TOKEN)
comandos = ['ayuda', 'help', 'bus']
descrip_comandos = ['el bot comienza a funcionar y da la bienvenida',
                    'se proporcionan diferentes opciones, como un contacto y la lista de comandos',
                    'igual que ayuda',
                    'devuelve el tiempo que le falta al bus, según la parada que marques en el inline keyboard'] 


@bot.message_handler(commands=['ayuda', 'help'])
def ayuda(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "Comandos", callback_data = "comandos"),
              InlineKeyboardButton(text = "Contacto", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(message.message.chat.id, "Con que necesitas ayuda, pequeña?", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def call_back(message):
    msg  = "COMANDOS: \n\n"
    for comando, descp in zip(comandos, descrip_comandos):
        msg += "/" + comando + ": \t" + descp + "\n"
    bot.send_message(message.message.chat.id, msg) 

        
#Responde a un mensaje que no es un comando
@bot.message_handler(content_types=["text"])
def comando_erroneo(message):
    if not message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        comando = 'Comando *NO* disponible'
        bot.send_message(message.chat.id, comando, parse_mode="MarkdownV2")


# EMT
#@bot.message_handler(commands=['bus'])
#def send_welcome(message):
 #   markup = InlineKeyboardMarkup()
  #  markup.add(InlineKeyboardButton(text = "Conde De Casal", callback_data = "condeCasal"),
   #            InlineKeyboardButton(text = "Polideportivo UPM", callback_data = "polideportivoUPM"))
    #bot.send_message(message.chat.id, "Qué Parada quieres consultar?")   


#FUNCIONALIDADES, 2 OPCIONES: EMT y PUERTA CORE


# PUERTA CORE



#Main
if __name__ == '__main__':
    print('Iniciando el bot')
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "EMT", callback_data = "comandos"),
               InlineKeyboardButton(text = "CORE_DOOR", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(clientId, "Eyy, bienvenido al bot personal de Core, Con que necesitas ayuda, pequeña?", reply_markup=markup)
    bot.infinity_polling()
    print('fin')