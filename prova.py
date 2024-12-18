import datetime
import secrets
import string

def provaFunc():
    return "PROVA FUNC"

print("HOLA")
alphabet = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
# Generar un token de 16 caracteres (puedes ajustar el tamaño)
token = ''.join(secrets.choice(alphabet) for _ in range(64))
print(token)
print(token)
print(token)


