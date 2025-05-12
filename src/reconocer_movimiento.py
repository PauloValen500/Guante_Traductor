# reconocer_movimiento.py
# Este archivo contiene funciones para reconocer letras que implican movimiento
# usando datos del giroscopio calibrado en una mano derecha

def detectar_letra_j(gyro):
    """
    Letra J (mano derecha): Movimiento descendente y curva hacia adentro (forma de gancho).
    gy negativo, gz positivo.
    """
    if gyro["gy"] < -200 and gyro["gz"] > 150:
        return True
    return False

def detectar_letra_z(gyro):
    """
    Letra Z (mano derecha): Movimiento tipo zigzag: derecha y luego abajo.
    gx positivo, gy negativo.
    """
    if gyro["gx"] > 200 and gyro["gy"] < -200:
        return True
    return False

def detectar_letra_k(gyro):
    """
    Letra K (mano derecha): Movimiento recto hacia arriba y giro hacia afuera.
    gy positivo, gz negativo.
    """
    if gyro["gy"] > 200 and gyro["gz"] < -150:
        return True
    return False

def detectar_letra_ñ(gyro):
    """
    Letra Ñ (mano derecha): Movimiento circular hacia afuera.
    gx positivo, gz negativo.
    """
    if gyro["gx"] > 150 and gyro["gz"] < -150:
        return True
    return False

def detectar_letra_q(gyro):
    """
    Letra Q (mano derecha): Movimiento descendente con giro hacia afuera.
    gy negativo, gz negativo.
    """
    if gyro["gy"] < -200 and gyro["gz"] < -100:
        return True
    return False

def detectar_letra_x(gyro):
    """
    Letra X (mano derecha): Movimiento cruzado rápido.
    gx y gy con valores altos (positivos o negativos).
    """
    if abs(gyro["gx"]) > 200 and abs(gyro["gy"]) > 200:
        return True
    return False

def detectar_letra_y(gyro):
    """
    Letra Y (mano derecha): Movimiento hacia arriba y giro hacia adentro.
    gy positivo, gz positivo.
    """
    if gyro["gy"] > 200 and gyro["gz"] > 100:
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
    if detectar_letra_k(gyro):
        return "K"
    if detectar_letra_ñ(gyro):
        return "Ñ"
    if detectar_letra_q(gyro):
        return "Q"
    if detectar_letra_x(gyro):
        return "X"
    if detectar_letra_y(gyro):
        return "Y"
    return None  # No se reconoce ningún patrón aún
