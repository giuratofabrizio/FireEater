import telebot
import json
from datetime import datetime

bot = telebot.TeleBot("token")

with open("./ListaIDTelebot.json") as f:
    lista_id = json.loads(f.read())
for id in lista_id:
    bot.send_message(id, "Fire Alert Attivato\nLuogo: Istituto di Istruzione Superiore Luigi Galvani, Via Gatti 14 (Niguarda, MI)\nData - Orario: {}".format(datetime.now()))