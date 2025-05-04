from sensor_dedos import leer_dedos

# Plantilla esperada para representar la letra "A"
plantilla_A = {
    "Gordo": "No doblado",
    "Índice": "Completamente doblado",
    "Medio": "Completamente doblado",
    "Anular": "Completamente doblado",
    "Meñique": "Completamente doblado"
}

# Compara los estados actuales de los dedos con una plantilla
def es_letra(letra_plantilla, estados_dedos):
    for dedo, estado_esperado in letra_plantilla.items():
        if estados_dedos[dedo]["estado"] != estado_esperado:
            return False
    return True

# Función que evalúa los dedos y devuelve la letra reconocida si coincide
def reconocer_letra():
    estados = leer_dedos()
    
    if es_letra(plantilla_A, estados):
        return "A"
    
    return None  # Si no coincide con ninguna letra
