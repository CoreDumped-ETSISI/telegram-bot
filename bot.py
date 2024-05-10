import telebot
import json 
import requests
from telebot.types import *
from constants import TOKEN
from bs4 import BeautifulSoup
import re


bot = telebot.TeleBot(TOKEN)


comandos = ['start', 'ayuda', 'help', 'bus']
descrip_comandos = ['el bot comienza a funcionar y da la bienvenida, además de un panel con la mayoria de las funcionalidades',
                    'se proporcionan diferentes opciones, como un contacto y la lista de comandos',
                    'igual que ayuda',
                    'devuelve el tiempo que le falta al bus, según la parada que marques en el inline keyboard'] 


@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "BUS E", callback_data = "busE"),
               InlineKeyboardButton(text = "CORE ABIERTO?", callback_data = "coreAbierto"),
               InlineKeyboardButton(text = "COMANDOS", callback_data = "comandos"),
              InlineKeyboardButton(text = "CONTACTO", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(message.chat.id, "Eyy, bienvenido al bot personal de Core, que necesitas?", reply_markup=markup)


@bot.message_handler(commands=['ayuda', 'help'])
def ayuda(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "COMANDOS", callback_data = "comandos"),
              InlineKeyboardButton(text = "CONTACTO", url =  "https://web.telegram.org/k/#@CoreDumpedUPM"))
    bot.send_message(message.chat.id, "Con que necesitas ayuda, pequeña?", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call:call.data=='comandos' )
def call_back(call):
    msg  = "COMANDOS: \n\n"
    for comando, descp in zip(comandos, descrip_comandos):
        msg += "/" + comando + ": \t" + descp + "\n"
    bot.send_message(call.message.chat.id, msg) 
     
    
    
@bot.callback_query_handler(func=lambda call:call.data=='coreAbierto' )
def call_back(call):
    bot.send_message(call.message.chat.id, "Este comando todavía no ha sido diseñado") 

# EMT BUS E
@bot.message_handler(commands=['bus'])
def busE(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "Conde De Casal", callback_data = "condeCasal"),
              InlineKeyboardButton(text = "Polideportivo UPM", callback_data = "polideportivoUPM"))
    bot.send_message(message.chat.id, "Qué Parada quieres consultar? \n Este procedimiento puede tardar varios segundos", reply_markup=markup) 
    
@bot.callback_query_handler(func=lambda call:call.data=='busE' )  # IGUAL QUE COMANDO BUS, PERO PARA EL INLINEKEYBOARD DE START
def call_back(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text = "Conde De Casal", callback_data = "condeCasal"),
              InlineKeyboardButton(text = "Polideportivo UPM", callback_data = "polideportivoUPM"))
    bot.send_message(call.message.chat.id, "Qué Parada quieres consultar? \n Este procedimiento puede tardar varios segundos", reply_markup=markup) 
    
    
URL_Polideportivo = 'https://cuantoqueda.com/parada/4281/linea/E/'

@bot.callback_query_handler(func=lambda call:call.data=='polideportivoUPM' )  
def call_back(call):  
    polideportivo =  requests.get(URL_Polideportivo).text
    soup_Poliportivo = BeautifulSoup(polideportivo, "html.parser") 
    tiempo_Polideportivo = regex(str(soup_Poliportivo.find_all('p')[3]))
    bot.send_message(call.message.chat.id, tiempo_Polideportivo)
    
URL_CondeCasal_E = 'https://cuantoqueda.com/parada/2603/linea/E/'
URL_CondeCasal_145 = 'https://cuantoqueda.com/parada/2603/linea/145/'

@bot.callback_query_handler(func=lambda call:call.data=='condeCasal' )  
def call_back(call):  
    condeCasal_E =  requests.get(URL_CondeCasal_E).text
    condeCasal_145 =  requests.get(URL_CondeCasal_145).text
    
    soup_condeCasal_E = BeautifulSoup(condeCasal_E, "html.parser").find_all('p')[3]
    soup_condeCasal_145 = BeautifulSoup(condeCasal_145, "html.parser").find_all('p')[3] 
    
    tiempo_condeCasal_E = regex(str(soup_condeCasal_E))
    tiempo_condeCasal_145 = regex(str(soup_condeCasal_145))
    
    tiempos_condeCasal = tiempo_condeCasal_E + '\n\n' + tiempo_condeCasal_145
    bot.send_message(call.message.chat.id, tiempos_condeCasal)

def regex(texto):
    patron = r"<\/?p[^>]*>"
    texto = re.sub(patron, "", texto)
    texto = eliminar_emojis(texto)
    return texto


def eliminar_emojis(cadena):
    patron = re.compile("✅")
    return patron.sub(r'', cadena)
    
# MENSAJE INCORRECTO
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




# MAIN
if __name__ == '__main__':
    print('Iniciando el bot')
    
    bot.infinity_polling()
      
    print('fin')
    