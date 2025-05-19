import urequests
import ujson

# Reemplaza esto con tu token actual
TOKEN = "eyJ0eXAiOiAiSldUIiwgImFsZyI6ICJSUzI1NiIsICJraWQiOiAiYWYyZGJjNTY1ZTQ0OTg5YmJmZDk5MjIwZjI5MTFmNjgzNmZhMTE2MiJ9.eyJpc3MiOiAiZmlyZWJhc2UtYWRtaW5zZGstZmJzdmNAZ3VhbnRlLXRyYWR1Y3Rvci1lZTI0Yy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsICJzdWIiOiAiZmlyZWJhc2UtYWRtaW5zZGstZmJzdmNAZ3VhbnRlLXRyYWR1Y3Rvci1lZTI0Yy5pYW0uZ3NlcnZpY2VhY2NvdW50LmNvbSIsICJpYXQiOiAxNzQ3MDkzNzQxLCAiZXhwIjogMTc0NzA5NzM0MSwgImF1ZCI6ICJodHRwczovL2ZpcmVzdG9yZS5nb29nbGVhcGlzLmNvbS8ifQ.VbrTEGLIdzygHneR5KH53C4vouhqRwnq1QfJYYSmJ2dNC05uSO1uZ8FrdeieT1sCos0SLkmEZmS6dy6S0m-xO9wJkn92RlWAZL7Gs9airnRFW5klnhTfc_63vQuXcrfKrpxa8HEOSCVTHLGSK6_fhbb9WlpdJtGK6cdrX6mYDPVBSqB-ieOCgNprwiIKSwfzJmLNgyQ4YDQXOu95_BbdPASr3Bt_2xMJ6AJ7vWnX_2UxJESgSmp5FAz6yEVxOgk2x6F5UClVLV8F8T7o5-eEQPZ33eIjQB9-iMRp91mdq1qVwGsnGs6ZcwCAXLZnHqBUCIkauXlIlHals-yO7Ytqrg"

# URL de la colección Firestore
URL = "https://firestore.googleapis.com/v1/projects/guante-traductor-ee24c/databases/(default)/documents/letra_actual"

def enviar_dato_a_firestore(letra):
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    
    data = {
        "fields": {
            "letra": {
                "stringValue": letra
            }
        }
    }

    try:
        response = urequests.post(URL, headers=headers, data=ujson.dumps(data))
        print(f"Respuesta: {response.status_code} - {response.text}")
        response.close()
    except Exception as e:
        print(f"Error al enviar dato: {e}")