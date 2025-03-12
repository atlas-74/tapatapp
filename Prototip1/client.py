import requests

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

class Error:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return f"Error {self.code}: {self.description}"

class DAOUser:
    def __init__(self):
        self.username = ""

    def getUserByUsername(self, username):

        try:
            response = requests.get("http://localhost:10050/tapatapp/getuser", params={"username": username})
            
            if response.status_code == 200:

                user_data = response.json()
                return User(id=user_data['id'], username=user_data['username'], email=user_data['email'], password="")
            
            elif response.status_code == 404:

                return Error(code=404, description="Usuario no encontrado")
            elif response.status_code == 400:

                return Error(code=400, description="Parámetros incorrectos, se necesita 'username'")
            else:

                return Error(code=response.status_code, description="Error desconocido al conectar con el servidor")
        
        except requests.exceptions.RequestException as e:

            return Error(code=503, description=f"Error al conectar con el servidor: {e}")

class Vista:
    def __init__(self):
        self.daoUser = DAOUser()

    def getUsernameByConsole(self):

        return input("Introduce el nombre de usuario: ")

    def showInfoUser(self, user):

        print(f"Información del usuario: {user}")

    def showInfoError(self, error):

        print(f"Información de error: {error}")

vista = Vista()

username = vista.getUsernameByConsole()

result = vista.daoUser.getUserByUsername(username)

if isinstance(result, User):
    vista.showInfoUser(result)
else:
    vista.showInfoError(result)
