import requests
import random
from bs4 import BeautifulSoup
# Función para enviar la imagen y el nombre de un animal aleatorio

def gato(update, context):
    random_number = random.randint(1, 1000)  # Genera un número aleatorio para evitar el almacenamiento en caché
    url = f'https://cataas.com/cat?nocache={random_number}'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_url = url
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)

def perro(update, context):
    response = requests.get('https://random.dog/')
    soup = BeautifulSoup(response.text, 'html.parser')
    image_url = 'https://random.dog/' + soup.find('img')['src']    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)


def pato(update, context):
    random_number = random.randint(1, 1000)  # Genera un número aleatorio para evitar el almacenamiento en caché
    url = f'https://random-d.uk/api/randomimg?nocache={random_number}'    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image_url = url
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_url)
