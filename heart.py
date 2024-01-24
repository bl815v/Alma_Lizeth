import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from traduccion import *
from operacion import *
from ecuaciones import *
from aleatorio import *
from ayuda import *
from conversiones import *
from resumen import *
from voz import *

TOKEN = '' #Reemplazalo por tu token de bot ;)

# Configura el registro de eventos
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola ❤️")

# Función para manejar todos los mensajes de texto
def echo(update, context):
    text = update.message.text
    
    if text.startswith('/'):
        # Ignora los comandos
        return
#    context.bot.send_message(chat_id=update.effective_chat.id, text=text) #envia el mensaje que recibe
def main():
    # Crea una instancia del bot
    bot = telegram.Bot(token=TOKEN)
    # Crea el objeto Updater y pasa la instancia del bot
    updater = Updater(bot=bot, use_context=True)
    # Obtiene el despachador para registrar manejadores
    dispatcher = updater.dispatcher

    # Agrega manejadores de comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ayuda", ayuda))
        #de traduccion
    dispatcher.add_handler(CommandHandler("esp", esp))
    dispatcher.add_handler(CommandHandler("ing", ing))
    dispatcher.add_handler(CommandHandler("fra", fra))
    dispatcher.add_handler(CommandHandler("rus", rus))
    dispatcher.add_handler(CommandHandler("ita", ita))
    dispatcher.add_handler(CommandHandler("jap", jap))
    dispatcher.add_handler(CommandHandler("ale", ale))
    dispatcher.add_handler(CommandHandler("cor", cor))
    dispatcher.add_handler(CommandHandler("por", por))
        #operaciones
    dispatcher.add_handler(CommandHandler("operar", operar))
        #ecuaciones
    dispatcher.add_handler(CommandHandler("despejar", despejar))
    dispatcher.add_handler(CommandHandler("derivar", derivar))
        #aleatorio
    dispatcher.add_handler(CommandHandler("gato", gato))
    dispatcher.add_handler(CommandHandler("perro", perro))
    dispatcher.add_handler(CommandHandler("pato", pato))
        #conversiones
    dispatcher.add_handler(CommandHandler("pesos", pesos))
    dispatcher.add_handler(CommandHandler("dolares", dolares))
    dispatcher.add_handler(CommandHandler("euros", euros))
        #resumen
    dispatcher.add_handler(CommandHandler("resumir", resumir))
        #voz
    dispatcher.add_handler(CommandHandler("voz", voz))
        
    
    
    # Agrega un manejador para mensajes de texto
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Inicia el bot
    updater.start_polling()

    # Ejecuta el bot hasta que se presione Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()