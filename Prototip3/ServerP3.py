import secrets
import hashlib
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

# Dictionary to store tokens for each user
user_tokens = {}

def generate_token():
    """Generate a unique token."""
    random_string = secrets.token_hex(32)  # Generate a 64-character random string
    return hashlib.sha256(random_string.encode()).hexdigest()

def token_required(f):
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Access unauthorized"}), 401

        # Extract the token and validate it
        token_value = token.split(" ")[1]
        if token_value not in user_tokens.values():
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
        # Generate a token for the user and store it
        token = generate_token()
        user_tokens[username] = token
        return jsonify({"token": token, "user": user}), 200
    return jsonify({"error": "Invalid username or password"}), 401

@app.route('/prototip3/logout', methods=['POST'])
@token_required
def logout():
    data = request.json
    username = data.get('username')
    if username in user_tokens:
        del user_tokens[username]  # Remove the user's token
        return jsonify({"message": f"User {username} logged out successfully"}), 200
    return jsonify({"error": "User not logged in"}), 400

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