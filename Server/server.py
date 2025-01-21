from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email = ""):
        self.id = id    
        self.username = username    
        self.password = password
        self.email = email

    def __str__(self):
        return "Id:" + str(self.id) + "  Username: " + str(self.username) + "  Password: " + self.password + "  Email: " + str(self.email)

listUsers= [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2, "usuari2", "123", "user2@proven.cat"),
    User(3, "admin", "12", "admin@proven.cat"),  
    User(4, "admin2", "12")
]

class DAOUsers:
    def __init__(self):
         self.users=listUsers

    def getUserByUsername(self, username):
        # cercar a la llista el User per username
        # return User     
        # return None
        for user in listUsers:
            if user.username == username:
                return user
            
        
daoUser = DAOUsers()

print(daoUser.getUserByUsername("usuari1"))
u=daoUser.getUserByUsername("notrobat")
if(u):
    print(u)
else:
    print("No trobat")

app = Flask(__name__)  

@app.route('/lista', methods=['GET'])
def hello():
    return "Hello World"

# Content-Type: application/x-www-form-urlencoded
@app.route("/provapost", methods=["POST"])
def provapost():
    username = request.form.get('username')  
    print(request.form.listvalues)
    return jsonify(username), 200

if __name__ == '__main__':
    app.run(debug=True)