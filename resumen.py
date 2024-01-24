import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

def resumir_texto(texto, num_oraciones):
    # Preprocesamiento del texto
    texto = texto.lower()
    frases = sent_tokenize(texto)
    palabras_stop = set(stopwords.words('spanish'))
    # Cálculo de la importancia de las frases
    importancia = {}
    for i, frase in enumerate(frases):
        palabras = frase.split()
        importancia[i] = sum(1 for palabra in palabras if palabra not in palabras_stop)
    # Selección de las frases más importantes
    frases_seleccionadas = sorted(importancia, key=importancia.get, reverse=True)[:num_oraciones]    
    # Generación del resumen
    resumen = ' '.join([frases[i] for i in frases_seleccionadas])
    return resumen

def resumir(update, context):
    mensaje = update.message.reply_to_message.text
    if len(context.args) > 0:
        try:
            num_oraciones = int(context.args[0])
        except ValueError:
            num_oraciones = 2     
    else:
        num_oraciones = 2     
        
    resumen = resumir_texto(mensaje, num_oraciones)
    # Enviar el resumen como respuesta
    context.bot.send_message(chat_id=update.effective_chat.id, text=resumen)
