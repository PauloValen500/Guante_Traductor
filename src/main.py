from reconocer_letra import reconocer_letra
from sensor_dedos import inicializar_sensores, leer_dedos
from time import sleep


# Inicializa los sensores flex
inicializar_sensores()

while True:
    letra = reconocer_letra()
    estados = leer_dedos()
    
    print("\nLecturas de sensores:")
    for dedo, info in estados.items():
        print(f"{dedo}: {info['estado']} (Lectura: {info['lectura']})")

    if letra:
        print(f"Letra detectada: {letra}")
    else:
        print("Ninguna letra reconocida")

    sleep(2)
