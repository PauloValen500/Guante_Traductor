from time import sleep
from sensor_dedos import inicializar_sensores
from reconocer_letra import reconocer_letra

inicializar_sensores()

while True:
    letra = reconocer_letra()
    if letra:
        print(f"Letra reconocida: {letra}")
    else:
        print("No se reconoció ninguna letra")
    sleep(2)
