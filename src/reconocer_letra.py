from sensor_dedos import leer_dedos

# Plantillas esperadas para representar las letras A, B, C, D y E
plantilla_A = {
    "Gordo": "No doblado",
    "Índice": "Completamente doblado",
    "Medio": "Completamente doblado",
    "Anular": "Completamente doblado",
    "Meñique": "Completamente doblado"
}

plantilla_B = {
    "Gordo": "Completamente doblado",
    "Índice": "No doblado",
    "Medio": "No doblado",
    "Anular": "No doblado",
    "Meñique": "No doblado"
}

plantilla_C = {
    "Gordo": "Medianamente doblado",
    "Índice": "Medianamente doblado",
    "Medio": "Medianamente doblado",
    "Anular": "Medianamente doblado",
    "Meñique": "Medianamente doblado"
}

plantilla_D = {
    "Gordo": "Completamente doblado",
    "Índice": "No doblado",
    "Medio": "Completamente doblado",
    "Anular": "Completamente doblado",
    "Meñique": "Completamente doblado"
}

plantilla_E = {
    "Gordo": "Completamente doblado",
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
    if es_letra(plantilla_B, estados):
        return "B"
    if es_letra(plantilla_C, estados):
        return "C"
    if es_letra(plantilla_D, estados):
        return "D"
    if es_letra(plantilla_E, estados):
        return "E"

    return None  # Si no coincide con ninguna letra
