from math import sqrt
# Función para manejar la operación matemática
def operar(update, context):
    text = update.message.reply_to_message.text
    text = text.replace('^', '**')
    result = eval(text, {"sqrt": sqrt})  # Evalúa la expresión matemática ingresada
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"El resultado es: {result}")
