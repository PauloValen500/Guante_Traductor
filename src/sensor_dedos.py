from machine import ADC, Pin
from time import sleep

# Configuración de pines y umbrales para cada dedo
config_dedos = {
    "Gordo":    {"pin": 36, "no_doblado": 200, "doblado": 2000},
    "Índice":   {"pin": 39, "no_doblado": 250, "doblado": 1200},
    "Medio":    {"pin": 34, "no_doblado": 300, "doblado": 600},
    "Anular":   {"pin": 35, "no_doblado": 280, "doblado": 1200},
    "Meñique":  {"pin": 32, "no_doblado": 230, "doblado": 2100}
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
