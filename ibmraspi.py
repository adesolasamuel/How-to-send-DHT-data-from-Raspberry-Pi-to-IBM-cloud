import paho.mqtt.client as mqtt
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
dhtDevice = adafruit_dht.DHT11(board.D4, use_pulseio=False)

ORG = "*******"
DEVICE_TYPE = "********" 
TOKEN = "******************"
DEVICE_ID = "*****************"

server = ORG + ".messaging.internetofthings.ibmcloud.com";
pubTopic1 = "iot-2/evt/Temperature/fmt/json";
pubTopic2 = "iot-2/evt/Humidity/fmt/json";
authMethod = "use-token-auth";
token = TOKEN;
clientId = "d:" + ORG + ":" + DEVICE_TYPE + ":" + DEVICE_ID;

mqttc = mqtt.Client(client_id=clientId)
mqttc.username_pw_set(authMethod, token)
mqttc.connect(server, 1883, 60)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature * 1.0
        temperature_f = temperature_c * (9 / 5) + 32.0
        humidity = dhtDevice.humidity * 1.0
        print(
            "Temp: {} F / {} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        
        mqttc.publish(pubTopic1, float(temperature_c))
        mqttc.publish(pubTopic2, humidity)
        print ("Published")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(5.0)

mqttc.loop_forever()
