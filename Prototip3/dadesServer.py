# Dades d'exemple amb List
# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email

users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com"),
    User(id=3, username="Hector", password="123", email="hhospital@gmail.com")
]

# Crear les classes Child, Tap, Role, Status i Treatment

class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def __str__(self):
        return "Child Id:" + str(self.id) + " Name:" + self.child_name

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6),
    Child(id=3, child_name="Hector Child", sleep_average=12, treatment_id=1, time=6)
]

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end
    
    def __str__(self):
        return f"Id: {self.id}, Child Id: {self.child_id}, Status Id: {self.status_id}, Init: {self.init}, End: {self.end}"

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2},
    {"user_id": 3, "child_id": 3, "rol_id": 1},
    {"user_id": 3, "child_id": 3, "rol_id": 2}
]

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def __str__(self):
        return "Role Id: " + str(self.id) + " Type Rol: " + self.type_rol

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

class Status:
    def __init__(self, id, child_id, name, status_id):
        self.id = id
        self.child_id = child_id
        self.name = name
        self.status_id = status_id

    def __str__(self):
        return "Status Id: " + str(self.status_id) + " Name: " + self.name + " Child Id: " + str(self.child_id)
    
statuses = [
    Status(id=1, child_id=1, name="sleep", status_id=1),
    Status(id=2, child_id=1, name="awake", status_id=2),
    Status(id=3, child_id=2, name="yes_eyepatch", status_id=3),
    Status(id=4, child_id=2, name="no_eyepatch", status_id=4)
]

class Treatment:
    def __init__(self, id, child_id, name):
        self.id = id
        self.child_id = child_id
        self.name = name

    def __str__(self):
        return "Treatment Id: " + str(self.id) + " Name: " + self.name

treatments = [
    Treatment(id=1, child_id=1, name='Hour'),
    Treatment(id=2, child_id=2, name='Percentage')
]