from sensor_gyro import inicializar_gyroscopo, leer_gyro
from reconocer_movimiento import reconocer_letra_por_movimiento
from time import sleep

gyro = inicializar_gyroscopo()

while True:
    datos_gyro = leer_gyro(gyro)
    letra_mov = reconocer_letra_por_movimiento(datos_gyro)

    if letra_mov:
        print(f"Letra detectada por movimiento: {letra_mov}")
    else:
        print("Sin movimiento reconocido")

    sleep(0.5)
