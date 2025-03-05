import requests

class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

class Child:
    def __init__(self, id, child_name, age):
        self.id = id
        self.child_name = child_name
        self.age = age

    def __str__(self):
        return f"Id: {self.id}, Name: {self.child_name}, Age: {self.age}"

class Tap:
    def __init__(self, id, child_id, timestamp):
        self.id = id
        self.child_id = child_id
        self.timestamp = timestamp

    def __str__(self):
        return f"Id: {self.id}, Child Id: {self.child_id}, Timestamp: {self.timestamp}"

class Error:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    def __str__(self):
        return f"Error {self.code}: {self.description}"

class DAOUser:
    def login(self, username, password):
        try:
            response = requests.post("http://localhost:5000/prototip2/login", json={"username": username, "password": password})
            if response.status_code == 200:
                user_data = response.json()
                return User(id=user_data['id'], username=user_data['username'], email=user_data['email'], password="")
            else:
                return Error(code=response.status_code, description=response.json().get("error", "Unknown error"))
        except requests.exceptions.RequestException as e:
            return Error(code=503, description=f"Error connecting to the server: {e}")

class DAOChild:
    def get_children_by_user_id(self, user_id):
        try:
            response = requests.get(f"http://localhost:5000/prototip2/children/{user_id}")
            if response.status_code == 200:
                children_data = response.json()
                return [Child(id=child['id'], child_name=child['child_name'], age=child['age']) for child in children_data]
            else:
                return Error(code=response.status_code, description="Error fetching children")
        except requests.exceptions.RequestException as e:
            return Error(code=503, description=f"Error connecting to the server: {e}")

class DAOTap:
    def get_taps_by_child_id(self, child_id):
        try:
            response = requests.get(f"http://localhost:5000/prototip2/taps/{child_id}")
            if response.status_code == 200:
                taps_data = response.json()
                return [Tap(id=tap['id'], child_id=tap['child_id'], timestamp=tap['timestamp']) for tap in taps_data]
            else:
                return Error(code=response.status_code, description="Error fetching taps")
        except requests.exceptions.RequestException as e:
            return Error(code=503, description=f"Error connecting to the server: {e}")

class Vista:
    def __init__(self):
        self.daoUser = DAOUser()
        self.daoChild = DAOChild()
        self.daoTap = DAOTap()

    def get_login_credentials(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        return username, password

    def show_info_user(self, user):
        print(f"User Info: {user}")

    def show_info_error(self, error):
        print(f"Error Info: {error}")

    def show_info_children(self, children):
        for child in children:
            print(f"Child Info: {child}")

    def show_info_taps(self, taps):
        for tap in taps:
            print(f"Tap Info: {tap}")

def main():
    vista = Vista()

    username, password = vista.get_login_credentials()
    result = vista.daoUser.login(username, password)

    if isinstance(result, User):
        vista.show_info_user(result)
        user_id = result.id
        children_result = vista.daoChild.get_children_by_user_id(user_id)
        if isinstance(children_result, list):
            vista.show_info_children(children_result)
            for child in children_result:
                taps_result = vista.daoTap.get_taps_by_child_id(child.id)
                if isinstance(taps_result, list):
                    vista.show_info_taps(taps_result)
                else:
                    vista.show_info_error(taps_result)
        else:
            vista.show_info_error(children_result)
    else:
        vista.show_info_error(result)

if __name__ == "__main__":
    main()
