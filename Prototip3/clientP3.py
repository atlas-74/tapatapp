import requests
import json
import os
import secrets  # Importamos la biblioteca para generar el token aleatorio

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class Child:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end

class Error:
    def __init__(self, code, description):
        self.code = code
        self.description = description

class DAOUser:
    def login(self, username, password):
        try:
            response = requests.post("http://localhost:5000/prototip3/login", json={"username": username, "password": password})
            if response.status_code == 200:
                data = response.json()
                # Generar un token aleatorio de 256 caracteres
                token = data['token']
                user_data = data['user']
                with open('Prototip3/token.txt', 'w') as f:
                    f.write(token)
                return token, User(id=user_data['id'], username=user_data['username'], email=user_data['email'], password="")
            else:
                return None, Error(code=response.status_code, description=response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            return None, Error(code=503, description=f"Error connecting to the server: {e}")

class DAOChild:
    def get_children_by_user_id(self, user_id, token):
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(f"http://localhost:5000/prototip3/GetChildByUser/{user_id}", headers=headers)
            if response.status_code == 200:
                return response.json(), None
            else:
                return None, Error(code=response.status_code, description=response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            return None, Error(code=503, description=f"Error connecting to the server: {e}")

def logout():
    try:
        os.remove('Prototip3/token.txt')
        print("Token removed successfully.")
    except FileNotFoundError:
        print("Token file not found.")

def main():
    dao_user = DAOUser()
    dao_child = DAOChild()

    try:
        with open('Prototip3/token.txt', 'r') as f:
            token = f.read()
    except FileNotFoundError:
        token = None

    if token:
        user_id = 1  # Assuming user_id is known or retrieved from somewhere
        children, error = dao_child.get_children_by_user_id(user_id, token)
        if children:
            print("Children:", children)
            logout_prompt = input("Cerrar sesión ? (S/N): ").strip().lower()
            if logout_prompt == 's':
                logout()
        else:
            print("Error:", error.description)
    else:
        username = input("Username: ")
        password = input("Password: ")
        token, user = dao_user.login(username, password)
        if token:
            print("Login successful!")
            children, error = dao_child.get_children_by_user_id(user.id, token)
            if children:
                print("Children:", children)
                logout_prompt = input("Cerrar sesión ? (S/N): ").strip().lower()
                if logout_prompt == 's':
                    logout()
            else:
                print("Error:", error.description)
        else:
            print("Login failed:", user.description)

if __name__ == "__main__":
    main()