from machine import I2C, Pin
import mpu6050
from time import sleep_ms

UMBRAL_RUIDO = 50
offsets = {"gx": 0, "gy": 0, "gz": 0}

def filtrar_ruido(valor):
    return 0 if abs(valor) < UMBRAL_RUIDO else valor

def inicializar_gyroscopo():
    global offsets
    i2c = I2C(0, scl=Pin(22), sda=Pin(21))
    sensor = mpu6050.accel(i2c)

    # Calibrar con más muestras
    suma = {"gx": 0, "gy": 0, "gz": 0}
    muestras = 100

    print("Calibrando giroscopio... No muevas el sensor.")
    for _ in range(muestras):
        datos = sensor.get_values()
        suma["gx"] += datos["GyX"]
        suma["gy"] += datos["GyY"]
        suma["gz"] += datos["GyZ"]
        sleep_ms(5)

    offsets = {
        "gx": suma["gx"] // muestras,
        "gy": suma["gy"] // muestras,
        "gz": suma["gz"] // muestras
    }

    print("Offsets calculados:", offsets)
    return sensor

def leer_gyro(sensor):
    datos = sensor.get_values()

    gx = filtrar_ruido(datos["GyX"] - offsets["gx"])
    gy = filtrar_ruido(datos["GyY"] - offsets["gy"])
    gz = filtrar_ruido(datos["GyZ"] - offsets["gz"])

    return {"gx": gx, "gy": gy, "gz": gz}
