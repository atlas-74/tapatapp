import dadesServer as dades
from dadesServer import User, Child, Tap, Status, Role, Treatment
from flask import Flask, jsonify, request

############  DAOs  ############

class UserDAO:
    def __init__(self):
        self.users = dades.users

    def getUserByLogin(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_children_by_user_id(self, user_id):
        child_ids = [rel["child_id"] for rel in dades.relation_user_child if rel["user_id"] == user_id]
        return [child.__dict__ for child in self.children if child.id in child_ids]

    def getChildById(self, child_id):
        for child in self.children:
            if child.id == child_id:
                return child.__dict__
        return None

class TapDAO:
    def __init__(self):
        self.taps = dades.taps

    def getTapByChild(self, child_id):
        return [tap.__dict__ for tap in self.taps if tap.child_id == child_id]

app = Flask(__name__)

user_dao = UserDAO()
child_dao = ChildDAO()
tap_dao = TapDAO()

TOKEN_VALID = "secret123"

def token_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or token.split(" ")[1] != TOKEN_VALID:
            return jsonify({"error": "Access unauthorized"}), 401
        return f(*args, **kwargs)
    decorated.__name__ = f.__name__
    return decorated

@app.route('/prototip3/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = user_dao.getUserByLogin(username, password)
    if user:
        return jsonify({"token": TOKEN_VALID, "user": user}), 200
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/prototip3/GetChildByUser/<int:user_id>', methods=['GET'])
@token_required
def get_children_by_user_id(user_id):
    children = child_dao.get_children_by_user_id(user_id)
    return jsonify(children), 200

@app.route('/prototip3/GetChildByChildId/<int:child_id>', methods=['GET'])
@token_required
def get_child_by_id(child_id):
    child = child_dao.getChildById(child_id)
    if child:
        return jsonify(child), 200
    return jsonify({"error": "Child not found"}), 404

@app.route('/prototip3/GetTapByChildId/<int:child_id>', methods=['GET'])
@token_required
def get_taps_by_child(child_id):
    taps = tap_dao.getTapByChild(child_id)
    return jsonify(taps), 200

if __name__ == '__main__':
    app.run(debug=True)