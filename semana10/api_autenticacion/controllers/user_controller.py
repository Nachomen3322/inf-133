from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
#hacemos handshake password hasheado, creando token
from werkzeug.security import check_password_hash


user_bp = Blueprint("user", __name__)

#creando endpoint que permita crear usuarios, restacatamos del cuerpo de la solicidos NO DEL FORMULARIO
@user_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400
    #buscando usuario
    existing_user = User.find_by_username(username)
    #si existe el usuario
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400
    #como no existe creamos el usuario por los datos mandados por el request
    new_user = User(username, password)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201

#creando ruta login para obtener el TOKEN
@user_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    #buscando usuario
    user = User.find_by_username(username)
    #si existe usuario, y la contraseña es igual al cifrado de la misma
    if user and check_password_hash(user.password_hash, password):
        # Si las credenciales son válidas, genera un token JWT
        #creat token, retorna token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401