import Adafruit_DHT
import telebot
from datetime import datetime
import json
bot = telebot.TeleBot("6390606092:AAHVH-cAokxfvnMbgI_FktakmkkMHAr3kGU")
DHT_SENSOR = Adafruit_DHT.AM2302
DHT_PIN = 4
verifica = True


def send_message(msg):
    with open("/home/pi/ListaIDTelebot.json") as f:
        lista_id = json.loads(f.read())
    for id in lista_id:
        bot.send_message(id, msg)
        
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if temperature < 24:
        verifica = True

    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        if temperature >= 24 and verifica == True:
            send_message("Fire Alert Attivato\nLuogo: Istituto di Istruzione Superiore Luigi Galvani, Via Gatti 14 (Niguarda, MI)\nAlle ore: {}".format(datetime.now()))
            verifica = False
    else:
        print("Failed to retrieve data from humidity sensor")




