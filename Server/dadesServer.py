
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
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

# Crear les classes Child, Tap, Role, Status i Treatment

class Child:
    def __init__(self, id, child_id, username):
        self.id=id
        self.child_id=child_id
        self.username=username

    def __str__(self):
        return "Child Id:" + str(self.child_id) + " Username:" + self.username


children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

class Tap:
    def __init__(self, child_id, status_id):
        self.child_id = child_id
        self.status_id = status_id
    
    def __str__(self):
        return " Child Id:" + str(self.child_id) + " Status Id:" + str(self.status_id)

taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=2, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]


relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2}
]

class Role:
    def __init__(self, username, type_rol):
        self.username = username
        self.type_rol = type_rol

    def __str__(self):
        return "Username: " + str(self.username) + " Type Rol:" + self.type_rol

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
        return "Status Id" + str(self.status_id) + " Name:" + self.name + " Child Id:" + str(self.child_id)
    
statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

class Treatment:
    def __init__(self, child_id, id, name):
        self.id = id
        self.child_id = child_id
        self.name = name

    def __str__(self):
        return "Id:" + str(self.id) + " Name:" + self.name

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]

