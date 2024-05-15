#EL FLOW MODIFICANDO MODELO -> VISTA -> CONTROLADOR
from flask import Blueprint, request, redirect, url_for, flash
#lo del import son decoradores que nos permitira manejas la sesion
from flask_login import login_user, logout_user, login_required
#para eñ desencriptado
from werkzeug.security import check_password_hash



# Importamos la vista de usuarios
from views import user_view

# Importamos el modelo de usuario
from models.user_model import User

# Un Blueprint es un objeto que agrupa
# rutas y vistas
user_bp = Blueprint("user", __name__)


# Ruta de la página raíz redirige a
# la página de inicio de sesión, va directo a la raiz
@user_bp.route("/")
def index():
    return redirect(url_for("user.login"))


@user_bp.route("/users")
@login_required
def list_users():
    # Obtenemos todos los usuarios
    users = User.get_all()
    # Llamamos a la vista de usuarios
    return user_view.usuarios(users)




# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@user_bp.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        username = request.form["username"]
        password = request.form["password"]
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("user.create_user"))
        # Creamos un nuevo usuario
        user = User(first_name, last_name, username, password)
        user.set_password(password)
        # Guardamos el usuario
        user.save()
        flash("Usuario registrado exitosamente", "success")
        return redirect(url_for("user.list_users"))
    # Llamamos a la vista de registro
    return user_view.registro()
    


# Actualizamos la información del usuario por su id
# Ya estamos en la vista de actualizar
# por lo que obtenemos los datos del formulario
# y actualizamos la información del usuario
@user_bp.route("/users/<int:id>/update", methods=["GET", "POST"])
@login_required
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    if request.method == "POST":
        # Obtenemos los datos del formulario
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        # Actualizamos los datos del usuario
        user.first_name = first_name
        user.last_name = last_name
        # Guardamos los cambios
        user.update()
        return redirect(url_for("user.list_users"))
    return user_view.actualizar(user)


@user_bp.route("/users/<int:id>/delete")
@login_required
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.list_users"))


# Ruta para el inicio de sesión
@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.get_user_by_username(username)
        #auntenticacion, si existe
        if user and check_password_hash(user.password_hash, password):
            #este usuario existe y tiene poder en esto
            login_user(user)
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("user.list_users"))
        else:
            flash("Nombre de usuario o contraseña incorrectos", "error")
    return user_view.login()


# Ruta para cerrar sesión
#para autorizar y permitir 
@user_bp.route("/logout")
#el login requerido
#ha y que aplicar a todo lo que queremos restringir, siempre debajo de la ruta por prioridad
@login_required
def logout():
    logout_user()
    #cerrando la sesion
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("user.login"))