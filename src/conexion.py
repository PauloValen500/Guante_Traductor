import network
import time
from umqtt.simple import MQTTClient
from machine import Pin, ADC

# Datos de la conexión WiFi y MQTT
ssid = "ProfesoresTecNM-UF"
password = ""

# Función para conectar a la red WiFi
def wifi_conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        pass
    print('Conexion con el WIFI %s establecida' % ssid)
    print(wlan.ifconfig())
