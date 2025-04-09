import mysql.connector
from mysql.connector import Error

class DaoUser:
    def __init__(self, connection):
        """
        Constructor que recibe una conexión a la base de datos.
        """
        self.connection = connection

    def validate_user(self, username, password):
        """Valida si el usuario y contraseña son correctos."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            query = "SELECT id, username, email FROM User WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                return {"status": "success", "user": user}
            else:
                return {"status": "error", "message": "Usuario o contraseña incorrectos"}

        except Error as e:
            return {"status": "error", "message": f"Error al ejecutar la consulta: {e}"}

        finally:
            cursor.close()

# Ejemplo de uso
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
            dao_user = DaoUser(connection)
            result = dao_user.validate_user("mare", "mare")
            print(result)

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        if connection.is_connected():
            connection.close()