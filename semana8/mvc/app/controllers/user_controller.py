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
