import requests 
# Función para convertir el valor de pesos colombianos a dólares
def dolares(update, context):
    amount = float(update.message.reply_to_message.text)
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/COP')
    data = response.json()
    exchange_rate = data['rates']['USD']
    converted_amount = round(amount / exchange_rate,2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{amount} dolares son aproximadamente {converted_amount} pesos colombianos.")

def euros(update, context):
    amount = float(update.message.reply_to_message.text)
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/COP')
    data = response.json()
    exchange_rate = data['rates']['EUR']
    converted_amount = round(amount / exchange_rate,2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{amount} euros son aproximadamente {converted_amount} pesos colombianos.")

# Función para convertir el valor de dólares a pesos colombianos
def pesos(update, context):
    amount = float(update.message.reply_to_message.text)
    response = requests.get(f'https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    exchange_rate = data['rates']['COP']
    converted_amount = round(amount / exchange_rate,2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{amount} pesos colombianos son aproximadamente {converted_amount} dolares.")