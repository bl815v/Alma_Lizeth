from gtts import gTTS
import os

# Función para convertir texto a audio y enviarlo como nota de voz
def voz(update, context):
    # Obtener el texto a convertir en audio
    texto = update.message.reply_to_message.text
    
    # Generar el nombre de archivo de salida
    nombre_archivo = "audio_salida"
    archivo_salida = nombre_archivo + ".mp3"

    # Generar el archivo de audio
    tts = gTTS(texto, lang='es', tld='com')
    tts.save(archivo_salida)

    # Enviar el archivo de audio como nota de voz
    chat_id = update.message.chat_id
    context.bot.send_voice(chat_id=chat_id, voice=open(archivo_salida, 'rb'))

    # Eliminar el archivo después de enviarlo
    os.remove(archivo_salida)
    
    print("Archivo de audio enviado y eliminado correctamente.")