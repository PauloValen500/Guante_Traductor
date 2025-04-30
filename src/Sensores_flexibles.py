from machine import ADC, Pin
from time import sleep

# Configuración por dedo: nombre, pin y umbrales de lectura
config_dedos = {
    "Gordo":    {"pin": 36, "no_doblado": 200, "doblado": 3900},
    "Índice":   {"pin": 39, "no_doblado": 250, "doblado": 3900},
    "Medio":    {"pin": 34, "no_doblado": 300, "doblado": 3900},
    "Anular":   {"pin": 35, "no_doblado": 280, "doblado": 3900},
    "Meñique":  {"pin": 32, "no_doblado": 230, "doblado": 3900}
}

# Crear objetos ADC y configurar resolución/atenuación
for dedo in config_dedos.values():
    sensor = ADC(Pin(dedo["pin"]))
    sensor.atten(ADC.ATTN_11DB)
    sensor.width(ADC.WIDTH_12BIT)
    dedo["adc"] = sensor  # guardar el objeto ADC en la config

# Función para determinar el estado del dedo
def obtener_estado(lectura, no_doblado, doblado):
    if lectura < no_doblado:
        return "No doblado"
    elif lectura > doblado:
        return "Completamente doblado"
    else:
        return "Medianamente doblado"

while True:
    print("\n=== Estado de los dedos ===")
    for nombre, dedo in config_dedos.items():
        lectura = dedo["adc"].read()
        estado = obtener_estado(lectura, dedo["no_doblado"], dedo["doblado"])
        print(f"{nombre}: {estado} (Lectura: {lectura})")
    print("===========================")
    sleep(2)
