#A ser rodado em uma IDE separada
import paho.mqtt.client as mqtt

BROKER = "broker.mqttdashboard.com"
TOPIC_SEND = "exp.criativas/pcparaespRay"
TOPIC_RECEIVE = "exp.criativas/espparapcRay"

def on_message(client, userdata, msg):
    print("Mensagem da ESP:", msg.payload.decode())
    client.publish(TOPIC_SEND, "STOP")  # manda parar

client = mqtt.Client("conectPC")
client.on_message = on_message
client.connect(BROKER)
client.subscribe(TOPIC_RECEIVE)
client.loop_forever()
