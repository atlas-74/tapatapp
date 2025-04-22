import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify, request

############  DAOs  ############

class UserDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_all_users(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT id, username, email FROM User"
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except Error as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()

    # Script para comprobar la conexión y los usuarios
if __name__ == "__main__":
    try:
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            database="tapatapp",
            user="root",
            password="root"
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            user_dao = UserDAO(connection)
            users = user_dao.get_all_users()

            if users:
                print("Usuarios en la base de datos:")
                for user in users:
                    print(f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
            else:
                print("No se encontraron usuarios en la base de datos.")

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("Conexión cerrada.")

    def get_user_by_login(self, username, password):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT id, username, email FROM User WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            return user
        except Error as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()


class ChildDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_all_children(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT * FROM Child"
            cursor.execute(query)
            children = cursor.fetchall()
            return children
        except Error as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()

    def get_children_by_user_id(self, user_id):
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = """
                SELECT c.id, c.child_name, c.sleep_average, c.treatment_id, c.time
                FROM Child c
                JOIN RelationUserChild ruc ON c.id = ruc.child_id
                WHERE ruc.user_id = %s
            """
            cursor.execute(query, (user_id,))
            children = cursor.fetchall()
            return children
        except Error as e:
            return {"status": "error", "message": str(e)}
        finally:
            cursor.close()


############  Flask App  ############

app = Flask(__name__)

# Configuración de la conexión a la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            database="tapatapp",
            user="root",
            password="root"
        )
        return connection
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


@app.route('/prototip2/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    connection = get_db_connection()
    if not connection:
        return jsonify({"status": "error", "message": "No se pudo conectar a la base de datos"}), 500

    user_dao = UserDAO(connection)
    user = user_dao.get_user_by_login(username, password)

    if user:
        return jsonify({"status": "success", "user": user}), 200
    else:
        return jsonify({"status": "error", "message": "Usuario o contraseña incorrectos"}), 400


@app.route('/prototip2/GetChildByUser/<int:user_id>', methods=['GET'])
def get_children_by_user_id(user_id):
    connection = get_db_connection()
    if not connection:
        return jsonify({"status": "error", "message": "No se pudo conectar a la base de datos"}), 500

    child_dao = ChildDAO(connection)
    children = child_dao.get_children_by_user_id(user_id)

    if children:
        return jsonify({"status": "success", "children": children}), 200
    else:
        return jsonify({"status": "error", "message": "No se encontraron niños para este usuario"}), 404


if __name__ == '__main__':
    app.run(debug=True)