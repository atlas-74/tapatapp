import requests

# Clase User que refleja la entidad User del diagrama de clases
class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

# Clase Error que maneja la información de error según el diagrama de clases
class Error:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return f"Error {self.code}: {self.description}"

# Clase DAOUser que maneja la lógica de acceso a los datos
class DAOUser:
    def __init__(self):
        self.username = ""

    def getUserByUsername(self, username):
        # Hacemos una solicitud HTTP para obtener la información del usuario
        try:
            response = requests.get("http://localhost:10050/tapatapp/getuser", params={"username": username})
            
            if response.status_code == 200:
                # Parseamos los datos de la respuesta
                user_data = response.json()
                return User(id=user_data['id'], username=user_data['username'], email=user_data['email'], password="")  # La contraseña no la necesitamos aquí
            
            elif response.status_code == 404:
                # Si el servidor responde con error 404, el usuario no fue encontrado
                return Error(code=404, description="Usuario no encontrado")
            elif response.status_code == 400:
                # Si el servidor responde con error 400 (parámetro incorrecto)
                return Error(code=400, description="Parámetros incorrectos, se necesita 'username'")
            else:
                # Si hay otro tipo de error en la comunicación
                return Error(code=response.status_code, description="Error desconocido al conectar con el servidor")
        
        except requests.exceptions.RequestException as e:
            # Si el servidor no está disponible
            return Error(code=503, description=f"Error al conectar con el servidor: {e}")

# Clase Vista que maneja la interfaz de usuario y las interacciones
class Vista:
    def __init__(self):
        self.daoUser = DAOUser()

    def getUsernameByConsole(self):
        # Método para obtener el nombre de usuario desde la entrada de la consola
        return input("Introduce el nombre de usuario: ")

    def showInfoUser(self, user):
        # Mostrar la información del usuario en consola
        print(f"Información del usuario: {user}")

    def showInfoError(self, error):
        # Mostrar el error en consola si no se encuentra el usuario
        print(f"Información de error: {error}")

# Creación de la vista y demostración del flujo
vista = Vista()

# Obtener el nombre de usuario desde la consola
username = vista.getUsernameByConsole()

# Obtener el usuario desde DAOUser
result = vista.daoUser.getUserByUsername(username)

# Verificar si se obtuvo un objeto User o Error
if isinstance(result, User):
    vista.showInfoUser(result)
else:
    vista.showInfoError(result)
