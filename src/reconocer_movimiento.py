# Este archivo contiene funciones para reconocer letras que implican movimiento
# usando datos del giroscopio previamente calibrado


def detectar_letra_j(gyro):
    """
    Detecta un movimiento curvo hacia abajo y luego hacia adentro (forma de gancho).
    Ejemplo básico: movimiento descendente en gy y giro en gz.
    """
    if gyro["gy"] < -200 and abs(gyro["gz"]) > 150:
        return True
    return False

def detectar_letra_z(gyro):
    """
    Detecta movimiento tipo zigzag (eje X positivo, luego Y negativo).
    """
    if gyro["gx"] > 200 and gyro["gy"] < -200:
        return True
    return False

def reconocer_letra_por_movimiento(gyro):
    """
    Analiza el movimiento actual y devuelve la letra si se reconoce alguna.
    """
    if detectar_letra_j(gyro):
        return "J"
    if detectar_letra_z(gyro):
        return "Z"
    return None  # No se reconoce ningún patrón aún
