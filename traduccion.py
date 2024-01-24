from mtranslate import translate

# Función para manejar el comando /esp
def esp(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'es')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def ing(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'en')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def fra(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'fr')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def rus(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'ru')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def ita(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'it')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def jap(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'ja')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def ale(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'de')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def cor(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'ko')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)

def por(update, context):
    text = update.message.reply_to_message.text
    translated_text = translate(text, 'pt')
    context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)



