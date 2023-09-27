import telebot
import json

bot = telebot.TeleBot("token")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("a")
    with open("./ListaIDTelebot.json") as f:
        lista_id = json.loads(f.read())
        if message.chat.id not in lista_id:
            lista_id.append(message.chat.id)
    
    with open('./ListaIDTelebot.json', 'w') as f:
        f.write(json.dumps(lista_id))
        

bot.infinity_polling()