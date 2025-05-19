from machine import ADC, Pin
from time import sleep

# Configuración de pines y umbrales para cada dedo
config_dedos = {
    "Gordo":    {"pin": 36, "no_doblado": 150, "doblado": 1100},
    "Índice":   {"pin": 39, "no_doblado": 150, "doblado": 700},
    "Medio":    {"pin": 34, "no_doblado": 400, "doblado": 1000},
    "Anular":   {"pin": 35, "no_doblado": 580, "doblado": 1100},
    "Meñique":  {"pin": 32, "no_doblado": 530, "doblado": 1100}
}

# Inicializar sensores
def inicializar_sensores():  
    for dedo in config_dedos.values():
        sensor = ADC(Pin(dedo["pin"]))
        sensor.atten(ADC.ATTN_11DB)
        sensor.width(ADC.WIDTH_12BIT)
        dedo["adc"] = sensor

# Función para obtener el estado del dedo según la lectura
def obtener_estado(lectura, no_doblado, doblado):
    if lectura < no_doblado:
        return "No doblado"
    elif lectura > doblado:
        return "Completamente doblado"
    else:
        return "Medianamente doblado"

# Función principal que puedes importar y usar
def leer_dedos():
    estados = {}
    for nombre, dedo in config_dedos.items():
        lectura = dedo["adc"].read()
        estado = obtener_estado(lectura, dedo["no_doblado"], dedo["doblado"])
        estados[nombre] = {
            "estado": estado,
            "lectura": lectura
        }
    return estados
