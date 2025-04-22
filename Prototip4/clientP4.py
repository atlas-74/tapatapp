import requests
import hashlib

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"


class Child:
    def __init__(self, id, name, sleep_average, treatment_id, time):
        self.id = id
        self.name = name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def __str__(self):
        return f"Id: {self.id}, Name: {self.name}, Sleep Average: {self.sleep_average}, Treatment ID: {self.treatment_id}, Time: {self.time}"


class DAOUser:
    def hash_password(self, password):
        """
        Convierte una contraseña en su equivalente MD5.
        """
        md5_hash = hashlib.md5(password.encode())
        return md5_hash.hexdigest()

    def login(self, username, password):
        """
        Realiza el login del usuario enviando la contraseña encriptada en MD5.
        """
        try:
            hashed_password = self.hash_password(password)
            response = requests.post("http://localhost:5000/prototip2/login", json={"username": username, "password": hashed_password})
            if response.status_code == 200:
                user_data = response.json()["user"]
                return User(id=user_data['id'], username=user_data['username'], email=user_data['email'])
            else:
                return {"status": "error", "message": response.json().get("message", "Error desconocido")}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}


class DAOChild:
    def get_children_by_user_id(self, user_id):
        """
        Obtiene los niños asociados a un usuario por su ID.
        """
        try:
            response = requests.get(f"http://localhost:5000/prototip2/GetChildByUser/{user_id}")
            if response.status_code == 200:
                children_data = response.json()["children"]
                children = [
                    Child(
                        id=child["id"],
                        name=child["child_name"],
                        sleep_average=child["sleep_average"],
                        treatment_id=child["treatment_id"],
                        time=child["time"]
                    )
                    for child in children_data
                ]
                return children
            else:
                return {"status": "error", "message": response.json().get("message", "Error desconocido")}
        except requests.RequestException as e:
            return {"status": "error", "message": str(e)}


# Ejemplo de uso
if __name__ == "__main__":
    dao_user = DAOUser()
    dao_child = DAOChild()

    # Login del usuario
    username = input("Introduce el nombre de usuario: ")
    password = input("Introduce la contraseña: ")
    login_result = dao_user.login(username, password)

    if isinstance(login_result, User):
        print(f"Login exitoso: {login_result}")

        # Obtener los niños asociados al usuario
        children_result = dao_child.get_children_by_user_id(login_result.id)
        if isinstance(children_result, list):
            print("Niños asociados al usuario:")
            for child in children_result:
                print(child)
        else:
            print(f"Error al obtener los niños: {children_result['message']}")
    else:
        print(f"Error en el login: {login_result['message']}")