
import telegram
import telebot
from telegram.ext import *
SafeCam=telegram.Bot(token='537843373:AAFCe3L41_LpXxHwi5zGhnXpjL4Zwk1zuTw')
Bota=telebot.TeleBot(token='537843373:AAFCe3L41_LpXxHwi5zGhnXpjL4Zwk1zuTw')
SafeCam_updater=Updater(SafeCam.token)

def listener(bot, update):
    id = update.message.chat_id
    mensaje= update.message.text
    print ('ID: '+str(id)+ ' ' + 'MENSAJE: '+ mensaje)

def start(bot, update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="bienvenido al bot de seguridad")

def registro(bot, update):
#    photo = open('imagen1.jpg', 'rb')
    photo = open('logo.png', 'rb')
    chat_id=update.message.chat_id
    Bota.send_photo(chat_id, photo)

def video(bot, update):
#    photo = open('imagen1.jpg', 'rb')
    video = open('output.avi', 'rb')
    chat_id=update.message.chat_id
    Bota.send_video(chat_id, video)

def archivo(bot, update):
    archivo=open('Informe.pdf', 'rb')
    chat_id=update.message.chat_id
    Bota.send_document(chat_id, archivo)



listener_handler= MessageHandler(Filters.text, listener)
start_handler=CommandHandler('start', start)
registro_handler=CommandHandler('registro', registro)
video_handler=CommandHandler('video', video)
archivo_handler=CommandHandler('archivo', archivo)
dispatcher=SafeCam_updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(listener_handler)
dispatcher.add_handler(registro_handler)
dispatcher.add_handler(video_handler)
dispatcher.add_handler(archivo_handler)
SafeCam_updater.start_polling()
SafeCam_updater.idle()
