import network
import time
from umqtt.simple import MQTTClient
from machine import Pin, ADC

# Datos de la conexión WiFi y MQTT
ssid = "Totalplay-669B"
password = "669B03DA272acp2y"
SERVER = "mqtt3.thingspeak.com"
puerto = 1883
id_canal = "2897693"
usuario = "NxMcNhwNNSAIDwsNCiUkNyQ"
id_cliente = "NxMcNhwNNSAIDwsNCiUkNyQ"
ip_password = "aKC7cQMHnvJBRTALqOttkcPf"

# Pines de conexión
pir_pin = Pin(4, Pin.IN)
ldr_pin = ADC(Pin(32))  # LDR conectado al pin 5 (analogico)

# Se crea el tópico MQTT
topicoCiclo = 'channels/' + id_canal + '/publish'

# Función para conectar a la red WiFi
def wifi_conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass
    print('Conexion con el WIFI %s establecida' % ssid)
    print(wlan.ifconfig())

# Función para conectar al servidor MQTT
def conectar_mqtt():
    cliente = MQTTClient(id_cliente, SERVER, puerto, usuario, ip_password)
    try:
        cliente.connect()
        print('MQTT conectado')
        return cliente
    except OSError as e:
        print("Error al conectar con MQTT:", e)
        return None

# Conectar a WiFi y MQTT
wifi_conecta()
