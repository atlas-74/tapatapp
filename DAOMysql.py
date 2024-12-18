from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Configuración de SQLAlchemy
Base = declarative_base()

# Modelo de la tabla "Rol"
class Rol(Base):
    __tablename__ = 'Rol'
    id = Column(Integer, primary_key=True)
    type_rol = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Rol(id={self.id}, type_rol='{self.type_rol}')>"

# Modelo de la tabla "Child"
class Child(Base):
    __tablename__ = 'Child'
    id = Column(Integer, primary_key=True)
    child_name = Column(String(50), nullable=False)
    sleep_average = Column(Integer, nullable=False)
    treatment_id = Column(Integer, ForeignKey('Treatment.id'))
    time = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Child(id={self.id}, child_name='{self.child_name}', sleep_average={self.sleep_average}, treatment_id={self.treatment_id}, time={self.time})>"

# Modelo de la tabla "User"
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    id_rol = Column(Integer, ForeignKey('Rol.id'))

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', id_rol={self.id_rol})>"

# Modelo de la tabla "RelationUserChild"
class RelationUserChild(Base):
    __tablename__ = 'RelationUserChild'
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    child_id = Column(Integer, ForeignKey('Child.id'), primary_key=True)
    rol_id = Column(Integer, ForeignKey('Rol.id'), primary_key=True)

    def __repr__(self):
        return f"<RelationUserChild(user_id={self.user_id}, child_id={self.child_id}, rol_id={self.rol_id})>"

# Modelo de la tabla "Treatment"
class Treatment(Base):
    __tablename__ = 'Treatment'
    id = Column(Integer, primary_key=True)
    name = Column(String(11), nullable=False)

    def __repr__(self):
        return f"<Treatment(id={self.id}, name='{self.name}')>"

# DAO para gestionar User, Child y sus relaciones
class UserChildDAO:
    def __init__(self, session):
        self.session = session

    # Crear un nuevo usuario
    def crear_usuario(self, username, password, email, id_rol):
        usuario = User(username=username, password=password, email=email, id_rol=id_rol)
        self.session.add(usuario)
        self.session.commit()
        return usuario

    # Crear un nuevo niño
    def crear_child(self, child_name, sleep_average, treatment_id, time):
        child = Child(child_name=child_name, sleep_average=sleep_average, treatment_id=treatment_id, time=time)
        self.session.add(child)
        self.session.commit()
        return child

    # Relacionar usuario con un niño y un rol
    def relacionar_usuario_child(self, user_id, child_id, rol_id):
        relacion = RelationUserChild(user_id=user_id, child_id=child_id, rol_id=rol_id)
        self.session.add(relacion)
        self.session.commit()
        return relacion

    # Obtener todos los niños relacionados con un usuario
    def obtener_children_por_usuario(self, user_id):
        relaciones = self.session.query(RelationUserChild).filter_by(user_id=user_id).all()
        return [relacion.child_id for relacion in relaciones]

    # Obtener los usuarios relacionados con un niño
    def obtener_usuarios_por_child(self, child_id):
        relaciones = self.session.query(RelationUserChild).filter_by(child_id=child_id).all()
        return [relacion.user_id for relacion in relaciones]

    # Listar todos los usuarios
    def listar_usuarios(self):
        return self.session.query(User).all()

    # Listar todos los niños
    def listar_children(self):
        return self.session.query(Child).all()

# Configuración de la base de datos
def main():
    engine = create_engine('mysql+pymysql://root:root@localhost/tapatapp')  # Cambia los valores
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Ejemplo de uso del DAO
    dao = UserChildDAO(session)

    # Crear roles, usuarios y niños
#    rol_admin = Rol(type_rol="Admin")
#    session.add(rol_admin)
#    session.commit()

    user = dao.crear_usuario(username="testuser", password="testpass", email="test@example.com", id_rol=rol_admin.id)
    child = dao.crear_child(child_name="TestChild", sleep_average=8, treatment_id=1, time=5)

    # Relacionar usuario y niño
    dao.relacionar_usuario_child(user_id=user.id, child_id=child.id, rol_id=rol_admin.id)

    # Listar usuarios
    usuarios = dao.listar_usuarios()
    for u in usuarios:
        print(u)

if __name__ == "__main__":
    main()
