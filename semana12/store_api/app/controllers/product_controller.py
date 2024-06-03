from flask import Blueprint, jsonify, request

# agregas el nombre del proyecto (app), aveces hay que
from models.product_model import Product
from utils.decorators import jwt_required, roles_required
from views.product_view import render_product_detail, render_product_list

# Crear un blueprint para el controlador de animales
product_bp = Blueprint("product", __name__)


@product_bp.route("/products", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_products():
    products = Product.get_all()
    return jsonify(render_product_list(products))


# Ruta para obtener un product específico por su ID
@product_bp.route("/products/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_product(id):
    product = Product.get_by_id(id)
    if product:
        return jsonify(render_product_detail(product))
    return jsonify({"error": "Producto no encontrado"}), 404


# Ruta para crear un nuevo product
@product_bp.route("/products", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_product():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Validación simple de datos de entrada
    if not name or not description or not price or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo product y guardarlo en la base de datos
    product = Product(name=name, description=description, price=price, stock=stock)
    product.save()

    return jsonify(render_product_detail(product)), 201


# Ruta para actualizar un product existente
@product_bp.route("/products/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_product(id):
    product = Product.get_by_id(id)

    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Actualizar los datos del product
    product.update(name=name, description=description, price=price, stock=stock)

    return jsonify(render_product_detail(product))


# Ruta para eliminar un product existente
@product_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_product(id):
    product = Product.get_by_id(id)

    if not product:
        return jsonify({"error": "Producto no encontrado"}), 404

    # Eliminar el product de la base de datos
    product.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
