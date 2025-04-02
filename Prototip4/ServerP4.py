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
        children_dicts = []
        for child in self.children:
            children_dicts.append({
                'id': child.id,
                'child_name': child.child_name,
                'sleep_average': child.sleep_average,
                'treatment_id': child.treatment_id,
                'time': child.time
            })
        return children_dicts

    def get_children_by_user_id(self, user_id):
        child_ids = []
        for rel in dades.relation_user_child:
            if rel["user_id"] == user_id:
                child_ids.append(rel["child_id"])
        children_dicts = []
        for child in self.children:
            if child.id in child_ids:
                children_dicts.append({
                    'id': child.id,
                    'child_name': child.child_name,
                    'sleep_average': child.sleep_average,
                    'treatment_id': child.treatment_id,
                    'time': child.time
                })
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

@app.route('/prototip2/GetChildByUser/<int:user_id>', methods=['GET'])
def get_children_by_user_id(user_id):
    children = child_dao.get_children_by_user_id(user_id)
    return jsonify(children), 200

@app.route('/prototip2/GetChildByChildId/<int:child_id>', methods=['GET'])
def get_child_by_id(child_id):
    child = child_dao.getChildById(child_id)
    if child:
        return jsonify(child), 200
    return jsonify({"error": "Child not found"}), 404

@app.route('/prototip2/GetTapByChildId/<int:child_id>', methods=['GET'])
def get_taps_by_child(child_id):
    taps = tap_dao.getTapByChild(child_id)
    return jsonify(taps), 200

if __name__ == '__main__':
    app.run(debug=True)

