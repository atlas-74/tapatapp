from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import hashlib
import random
import datetime 
import secrets
import string



# Definim la base de models amb SQLAlchemy
Base = declarative_base()

# Model de la taula User
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    id_rol = Column(Integer, nullable=False, default=0)

# DAO per a la taula User
class UserDAO:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def add_user(self, username, password, email, id_rol=0):
        session = self.Session()
        try:
            new_user = User(username=username, password=password, email=email, id_rol=id_rol)
            session.add(new_user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_user_by_id(self, user_id):
        session = self.Session()
        try:
            return session.query(User).filter_by(id=user_id).first()
        finally:
            session.close()

    def get_all_users(self):
        session = self.Session()
        try:
            return session.query(User).all()
        finally:
            session.close()

    def get_users_paginated(self, page, per_page):
        session = self.Session()
        try:
            offset = (page - 1) * per_page
            return session.query(User).offset(offset).limit(per_page).all()
        finally:
            session.close()

    def search_users_by_username(self, username):
        session = self.Session()
        try:
            return session.query(User).filter(User.username.like(f"%{username}%")).all()
        finally:
            session.close()

    def update_user(self, user_id, **kwargs):
        session = self.Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if not user:
                return None
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            return user
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_user(self, user_id):
        session = self.Session()
        try:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                session.delete(user)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def login_user(self, user_name, user_passwd):
        session = self.Session()
        try:
            user = session.query(User).filter_by(username=user_name, password=user_passwd).first()
            if user:
                access_token = self.create_token()
                user.token = access_token  # Emmagatzema el token a la base de dades
                session.commit()
                return access_token

            return "Invalid credentials"
        except Exception as e:
            session.rollback()
            return "msg:" + str(e)
        finally:
            session.close()
    
    def create_token(self):
        #numeric_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        #input_string= identity + str(numeric_datetime)
        #encoded_string = input_string.encode('utf-8')
        #return hashlib.sha512(encoded_string).hexdigest()
        #token = secrets.token_hex(64)
        # Definir un alfabeto con letras mayúsculas, minúsculas y dígitos
        alphabet = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        # Generar un token de 16 caracteres (puedes ajustar el tamaño)
        token = ''.join(secrets.choice(alphabet) for _ in range(64))
        return token    

# Exemples d'ús del DAO
if __name__ == "__main__":
    # Base de dades MySQL per provar
    DATABASE_URL = "mysql+pymysql://root:root@localhost/tapatapp"

    dao = UserDAO(DATABASE_URL)

    # Afegir un nou usuari
    #dao.add_user(username="johndoe", password="password123", email="johndoe@example.com")

    # Obtenir usuaris paginats
    page = 1
    per_page = 5
    users = dao.get_users_paginated(page, per_page)
    for user in users:
        print(user.username, user.email)

    # Cercar usuaris per username
    search_results = dao.search_users_by_username("john")
    for user in search_results:
        print(f"Found: {user.username}, {user.email}")

    r = dao.login_user("johndoe","password123")
    print(r)
