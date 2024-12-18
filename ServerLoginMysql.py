from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Configuració de Flask
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"
jwt = JWTManager(app)

# Configuració de SQLAlchemy
Base = declarative_base()
DATABASE_URL = "mysql+pymysql://username:password@localhost/dbname"
engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))

# Model de la taula User
class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    id_rol = Column(Integer, nullable=False, default=0)
    token = Column(String(400), nullable=True)

Base.metadata.create_all(engine)

# Endpoint per a l'inici de sessió
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    session = Session()
    try:
        user = session.query(User).filter_by(username=username, password=password).first()
        if user:
            access_token = create_access_token(identity=username)
            user.token = access_token  # Emmagatzema el token a la base de dades
            session.commit()
            return jsonify(access_token=access_token), 200

        return jsonify({"msg": "Invalid credentials"}), 401
    except Exception as e:
        session.rollback()
        return jsonify({"msg": str(e)}), 500
    finally:
        session.close()

# Endpoint protegit
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    session = Session()
    try:
        username=request.headers.get("Username")
        print(username)
        user = session.query(User).filter_by(username=current_user, token=request.headers.get("Authorization").split()[1]).first()
        if user:
            return jsonify(logged_in_as=user.username, email=user.email, id_rol=user.id_rol), 200
        return jsonify({"msg": "Invalid token or user not found"}), 401
    finally:
        session.close()

if __name__ == "__main__":
    app.run(debug=True)