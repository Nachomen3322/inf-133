from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#usando herencia
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        #aca lo hace en el constructor, es valido igual
        self.password_hash = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    # Esta funcion encuentra un usuario por su nombre de usuario
    @staticmethod
    #que sea unico
    def find_by_username(username):
        #jalamos el usuario
        return User.query.filter_by(username=username).first()