import time
import board
import Adafruit_DHT
import telebot

# Initial the dht device, with data pin connected to:
dhtDevice = Adafruit_DHT.DHT22(board.D4)
bot = telebot.TeleBot("6390606092:AAHVH-cAokxfvnMbgI_FktakmkkMHAr3kGU")

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D24, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature


        if temperature_c > 21:
            send_message("Fire Alert Attivato\nLuogo: Istituto di Istruzione Superiore Luigi Galvani, Via Gatti 14 (Niguarda, MI)\nAlle ore: {}".format(datetime.now()))

        print(
            "Temp: {:.1f} C".format(
                temperature_c
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)

def send_message(msg):
    with open("./ListaIDTelebot.json") as f:
        lista_id = json.loads(f.read())
    for id in lista_id:
        bot.send_message(id, msg)