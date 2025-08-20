#A ser rodado no Thonny IDE
from machine import Pin
import time, network
from umqtt.simple import MQTTClient

# Configuração
MQTT_CLIENT_ID = "conectESP32"
MQTT_BROKER = "broker.mqttdashboard.com"
TOPIC_SEND = "exp.criativas/espparapcRay"
TOPIC_RECEIVE = "exp.criativas/pcparaespRay"

# WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(".", "........")
while not wifi.isconnected():
    pass
print("WiFi OK!")

# Pinos
echo = Pin(27, Pin.IN)
trig = Pin(21, Pin.OUT)
buzzer = Pin(32, Pin.OUT)
led = Pin(2, Pin.OUT)

stop_flag = False

def callback(topic, msg):
    global stop_flag
    msg = msg.decode()
    print("MQTT recebido:", msg)
    if msg == "STOP":
        stop_flag = True

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
client.set_callback(callback)
client.connect()
client.subscribe(TOPIC_RECEIVE)

def medir_distancia():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()

    return (time.ticks_diff(pulse_end, pulse_start) / 2) * 0.0343

# Medições
start = time.time()
ultima = medir_distancia()

while time.time() - start < 5 and not stop_flag:
    dist = medir_distancia()
    print("Distância:", dist)
    if abs(dist - ultima) > 20:
        client.publish(TOPIC_SEND, "Objeto mudou de posição!")
    ultima = dist
    client.check_msg()
    time.sleep(1)

if stop_flag:
    for i in range(3):
        led.value(1)
        buzzer.value(1)
        time.sleep(0.5)
        led.value(0)
        buzzer.value(0)
        time.sleep(0.5)

