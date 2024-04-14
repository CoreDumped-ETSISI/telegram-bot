import telebot
import requests
from telebot.types import *
from constants import TOKEN
import time

bot = telebot.TeleBot(TOKEN)
comandos = ['start', 'ayuda', 'help', 'bus']
descrip_comandos = ['el bot comienza a funcionar y da la bienvenida, además de un panel con la mayoria de las funcionalidades',
                    'se proporcionan diferentes opciones, como un contacto y la lista de comandos',
                    'igual que ayuda',
                    'devuelve el tiempo que le falta al bus, según la parada que marques en el inline keyboard'] 


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "BUS E", callback_data = "comandos"),
               InlineKeyboardButton(text = "CORE ABIERTO?", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"),
               InlineKeyboardButton(text = "COMANDOS", callback_data = "comandos"),
              InlineKeyboardButton(text = "CONTACTO", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(message.chat.id, "Eyy, bienvenido al bot personal de Core, que necesitas?", reply_markup=markup)


@bot.message_handler(commands=['ayuda', 'help'])
def ayuda(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "COMANDOS", callback_data = "comandos"),
              InlineKeyboardButton(text = "CONTACTO", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(message.chat.id, "Con que necesitas ayuda, pequeña?", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: True)
def call_back(message):
    msg  = "COMANDOS: \n\n"
    for comando, descp in zip(comandos, descrip_comandos):
        msg += "/" + comando + ": \t" + descp + "\n"
    bot.send_message(message.message.chat.id, msg) 

# EMT BUS E
@bot.message_handler(commands=['bus'])
def busE(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "Conde De Casal", callback_data = "condeCasal"),
              InlineKeyboardButton(text = "Polideportivo UPM", callback_data = "polideportivoUPM"))
    bot.send_message(message.chat.id, "Qué Parada quieres consultar?", reply_markup=markup) 
    
        
#Responde a un mensaje que no es un comando
@bot.message_handler(content_types=["text"])
def comando_erroneo(message):
    if not message.text.startswith("/"):
        bot.send_chat_action(message.chat.id, "typing")
        comando = 'Eso *NO* es un comado'
        bot.send_message(message.chat.id, comando, parse_mode="MarkdownV2")
    elif not message.text in comandos:
        bot.send_chat_action(message.chat.id, "typing")
        comando = 'Ese comado *NO* existe'
        bot.send_message(message.chat.id, comando, parse_mode="MarkdownV2")




# PUERTA CORE


#Main
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.infinity_polling()
    print('fin')