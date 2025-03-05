import dadesServer as dades
from dadesServer import User,Child,Tap,Status,Role,Treatment
from flask import Flask, jsonify, request

# Exemple d'ús de la llista d'usuaris
'''for x in dades.users:
    print(x)

# Exemple d'ús de la classe User
a= User(id=1, username="Kurl", password="12345", email="prova2@gmail.com")
print(a)'''

############  DAOs  ############

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def getUserByLogin(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        # Inicialitzar una llista buida per emmagatzemar els diccionaris dels fills
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            # Convertir l'objecte 'child' en diccionari i afegir-lo a la llista
            children_dicts.append(child.__dict__)
        return children_dicts

    def get_children_by_user_id(self, user_id):
        # Inicialitzar una llista buida per emmagatzemar els child_ids
        child_ids = []
        # Recórrer cada relació a la llista relation_user_child
        for rel in dades.relation_user_child:
            # Comprovar si el user_id de la relació coincideix amb el user_id donat
            if rel["user_id"] == user_id:
                # Afegir el child_id a la llista child_ids
                child_ids.append(rel["child_id"])
        # Inicialitzar una llista buida per emmagatzemar els diccionaris dels fills
        children_dicts = []
        # Recórrer cada objecte 'child' en la llista 'self.children'
        for child in self.children:
            # Comprovar si l'ID del child està dins de la llista child_ids
            if child.id in child_ids:
                # Afegir el diccionari de l'objecte child a la llista
                children_dicts.append(child.__dict__)
        return children_dicts

    def getChildById(self, child_id):
        for child in self.children:
            if child.id == child_id:
                return child.__dict__
        return None

class TapDAO:
    def __init__(self):
        self.taps = dades.taps

    def getTapByChild(self, child_id):
        taps_dicts = []
        for tap in self.taps:
            if tap.child_id == child_id:
                taps_dicts.append(tap.__dict__)
        return taps_dicts

app = Flask(__name__)

user_dao = UserDAO()
child_dao = ChildDAO()
tap_dao = TapDAO()

@app.route('/prototip2/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = user_dao.getUserByLogin(username, password)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/prototip2/children/<int:user_id>', methods=['GET'])
def get_children_by_user_id(user_id):
    children = child_dao.get_children_by_user_id(user_id)
    return jsonify(children), 200

@app.route('/prototip2/child/<int:child_id>', methods=['GET'])
def get_child_by_id(child_id):
    child = child_dao.getChildById(child_id)
    if child:
        return jsonify(child), 200
    return jsonify({"error": "Child not found"}), 404

@app.route('/prototip2/taps/<int:child_id>', methods=['GET'])
def get_taps_by_child(child_id):
    taps = tap_dao.getTapByChild(child_id)
    return jsonify(taps), 200

if __name__ == '__main__':
    app.run(debug=True)

