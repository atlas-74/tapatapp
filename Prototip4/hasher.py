import hashlib

def hash_password(password):
    """
    Convierte una contraseña en su equivalente MD5.
    """
    md5_hash = hashlib.md5(password.encode())
    return md5_hash.hexdigest()

# Ejemplo de uso
if __name__ == "__main__":
    password = input("Introduce la contraseña a convertir a MD5: ")
    hashed_password = hash_password(password)
    print(f"Contraseña original: {password}")
    print(f"Contraseña en MD5: {hashed_password}")