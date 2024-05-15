from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#cuanto es Mayuscua UserMixin es clase, MINUSCULA = funcion


# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos


#ESTAMOS HEREDANDO userMixin, a user herencia multiple por 2 clases, user y dbmodel
class User(UserMixin, db.Model):
    __tablename__ = "users"
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    #se guardara en shadow, encriptado, examen
    password_hash = db.Column(db.String(128), nullable=False)

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.set_password(password)

    # Genera un hash seguro de la contraseña
    # SIEMPRE GENERAMOS EL HASH EN EL MODELO, NO EN OTRO LADO
    #esta linea puede estar arriba, igual ambas son validas, hash = cadena encriptada de n caracteres
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()

    # Obtiene un usuario por su id
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    # Actualiza un usuario en la base de datos
    def update(self):
        db.session.commit()

    # Elimina un usuario de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Obtiene un usuario por su nombre de usuario
    #en el controlador validaremos que cuando se cree el usuario no exista el usuario
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()