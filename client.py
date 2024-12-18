import requests

# Paso 1: Autenticarse para obtener el token
login_url = "http://localhost:5000/login"
login_payload = {"username": "user1", "password": "password1"}

response = requests.post(login_url, json=login_payload)

if response.status_code == 200:
    # Extraer el token del JSON
    token = response.json().get("access_token")
    print(f"Token recibido: {token}")

    # Paso 2: Usar el token para acceder al endpoint protegido
    protected_url = "http://localhost:5000/protected"
    headers = {
        "Authorization": f"Bearer {token}",  # Incluir el token en el encabezado
        "Username": "user1 PROVA HEADER"  # Encabezado personalizado con el username
    }

    protected_response = requests.get(protected_url, headers=headers)

    if protected_response.status_code == 200:
        print("Respuesta del endpoint protegido:", protected_response.json())
    else:
        print("No se pudo acceder al endpoint protegido:", protected_response.status_code, protected_response.text)
else:
    print("Error al autenticarse:", response.status_code, response.text)
