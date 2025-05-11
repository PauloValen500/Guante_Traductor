from sensor_dedos import leer_dedos

# Diccionario de plantillas por letra
plantillas = {
    "A": {
        "Gordo": "No doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "B": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "No doblado",
        "Meñique": "No doblado"
    },
    "C": {
        "Gordo": "Medianamente doblado",
        "Índice": "Medianamente doblado",
        "Medio": "Medianamente doblado",
        "Anular": "Medianamente doblado",
        "Meñique": "Medianamente doblado"
    },
    "D": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "E": {
        "Gordo": "Completamente doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "F": {
        "Gordo": "No doblado",
        "Índice": "Medianamente doblado",
        "Medio": "No doblado",
        "Anular": "No doblado",
        "Meñique": "No doblado"
    },
    "G": {
        "Gordo": "No doblado",
        "Índice": "No doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "H": {
        "Gordo": "No doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "I": {
        "Gordo": "Completamente doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "No doblado"
    },
    "L": {
        "Gordo": "No doblado",
        "Índice": "No doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "M": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "No doblado",
        "Meñique": "Completamente doblado"
    },
    "N": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "O": {
        "Gordo": "Medianamente doblado",
        "Índice": "Medianamente doblado",
        "Medio": "Medianamente doblado",
        "Anular": "Medianamente doblado",
        "Meñique": "Medianamente doblado"
    },
    "P": {
        "Gordo": "No doblado",
        "Índice": "No doblado",
        "Medio": "Medianamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "R": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "S": {
        "Gordo": "Completamente doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "T": {
        "Gordo": "No doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "U": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "V": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "Completamente doblado",
        "Meñique": "Completamente doblado"
    },
    "W": {
        "Gordo": "Completamente doblado",
        "Índice": "No doblado",
        "Medio": "No doblado",
        "Anular": "No doblado",
        "Meñique": "Completamente doblado"
    },
    "Y": {
        "Gordo": "No doblado",
        "Índice": "Completamente doblado",
        "Medio": "Completamente doblado",
        "Anular": "Completamente doblado",
        "Meñique": "No doblado"
    }
}

# Compara los estados actuales con la plantilla
def es_letra(plantilla, estados_dedos):
    for dedo, estado_esperado in plantilla.items():
        if estados_dedos[dedo]["estado"] != estado_esperado:
            return False
    return True

# Detecta la letra
def reconocer_letra():
    estados = leer_dedos()
    for letra, plantilla in plantillas.items():
        if es_letra(plantilla, estados):
            return letra
    return None
