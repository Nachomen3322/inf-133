# Aca es lo principal, contruyendo, esto se define al final donde se mostrara
from flask import Blueprint, request, redirect, url_for


# importa la vista de usuarios
from views import user_view

# Importa el modelo de usuario
from models.user_model import User

# Definiendo blueprint, la maqueta que dice como se va construir la maquitas y vistas
# Se levanta cuando se inicializa
user_bp = Blueprint("user", __name__)


# definimos como se van a llamar las rutas
# aca llama funcion tras funcion
@user_bp.route("/")
def usuarios():
    # Obtenemostodos los usuarios
    users = User.get_all()
    # Lllamamos a la vista de usuaruis, la primera que se levante, y si users tiene algo muestra la lista, si no muestra vacio
    return user_view.usuarios(users)


# ESTA FUNCION NOS PERMITE REGISTRAR
# funcion asociada a registro
# se encarga de recibir 2 tipos de peticiones get or post
@user_bp.route("/users", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        # SE RESCATA LA INF DEL USER
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        fechanac = request.form["fechanac"]

        # Creamos un nuevo usuario
        user = User(first_name, last_name, email, password, fechanac)
        # Guardamos el usuario, se guarda asi mismo en la bd hace el commit
        user.save()
        # Redirigimos a la vista de usuarios, redirecciona a users.usuarios que es usuarios.html, no se usa html porque redireccionamos un link
        return redirect(url_for("user.usuarios"))
    # Llamamos a la vista de registro
    return user_view.registro()


# Actualizar la información de un usuario por su id
# primero recuperamos la información del usuario
# agarra users con parametro de entrada id diciendo que es un entero, protegido de entero
@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):
    # Obtenemos el usuario por su id
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    # envia el usuario a modificar
    return user_view.actualizar(user)


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
# Hay que hacer un post a users/id, el que ejectua el post es el usuario en el html
@user_bp.route("/users/<int:id>", methods=["POST"])
def actualizar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    # Obtenemos los datos del formulario
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]
    fechanac = request.form["fechanac"]
    # Actualizamos los datos del usuario
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.password = password
    user.fechanac = fechanac
    # Guardamos los cambios
    user.update()
    # redirecta al blueprint user, dentro del blueprint user, hay usuarios, haz que redireccione a la ruta usuarios, devuelve a la raiz
    return redirect(url_for("user.usuarios"))



@user_bp.route("/usersdelete/<int:id>", methods=["DELETE"])
def eliminar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.eliminate()
    # redirecta al blueprint user, dentro del blueprint user, hay usuarios, haz que redireccione a la ruta usuarios, devuelve a la raiz
    return redirect(url_for("user.usuarios"))
