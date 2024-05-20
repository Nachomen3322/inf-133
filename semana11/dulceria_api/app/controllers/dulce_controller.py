from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from models.user_model import User
from views.dulce_view import render_dulce_list, render_dulce_detail
from views.user_view import render_user_list, render_user_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
from utils.decorators import jwt_required, roles_required


# Crear un blueprint para el controlador de Dulces
dulce_bp = Blueprint("dulce", __name__)
user_bp = Blueprint("user", __name__)


@dulce_bp.route("/Dulces", methods=["GET"])
@jwt_required
def get_Dulces():
    Dulces = Dulce.get_all()
    return jsonify(render_dulce_list(Dulces))


# Ruta para obtener un dulce específico por su ID
@dulce_bp.route("/Dulces/<int:id>", methods=["GET"])
@jwt_required
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "Dulce no encontrado"}), 404


# Ruta para crear un nuevo dulce
@dulce_bp.route("/Dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    print(data)
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Validación simple de datos de entrada
    if not titulo or not autor or not edicion or disponibilidad is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo dulce y guardarlo en la base de datos
    dulce = Dulce(
        titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad
    )
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201


# Ruta para actualizar un dulce existente
@dulce_bp.route("/Dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Actualizar los datos del dulce
    dulce.update(
        titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad
    )

    return jsonify(render_dulce_detail(dulce))


# Ruta para eliminar un dulce existente
@dulce_bp.route("/Dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "Dulce no encontrado"}), 404

    # Eliminar el dulce de la base de datos
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204


@user_bp.route("/User", methods=["GET"])
@jwt_required
def get_Users():
    Users = User.get_all()
    return jsonify(render_user_list(Users))


# Ruta para obtener un dulce específico por su ID
@dulce_bp.route("/Users/<int:id>", methods=["GET"])
@jwt_required
def get_user(id):
    user = User.get_by_id(id)
    if user:
        return jsonify(render_user_detail(user))
    return jsonify({"error": "Dulce no encontrado"}), 404


# Ruta para crear un nuevo dulce
@dulce_bp.route("/Users", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_user():
    data = request.json
    print(data)
    username = username.get("username")
    password = password.get("password")
    roles = roles.get("roles")
    # Validación simple de datos de entrada
    if not username or not password or roles is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400
    # Crear un nuevo dulce y guardarlo en la base de datos
    user = User(
        username=username, password=password, roles=roles
    )
    user.save()
    return jsonify(render_user_detail(user)), 201


# Ruta para actualizar un dulce existente
@user_bp.route("/Users/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["user"])
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "User no encontrado"}), 404
    data = request.json
    username = data.get("username")
    password = data.get("password")
    roles = data.get("roles")
    user.update(username=username, password=password, roles=roles)
    return jsonify(render_user_detail(user))


@user_bp.route("/Users/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "User no encontrado"}), 404
    user.delete()
    return "", 204
