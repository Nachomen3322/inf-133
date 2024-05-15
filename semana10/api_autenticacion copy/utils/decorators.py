from flask import jsonify
#estamos metienado mas cositas al get ese, antes solo era el username, ahora mas cosas
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps
import json


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper

#DECORADOR CON VARIABLE DE ENTRADA, una enviando un array   
def roles_required(roles=[]):
    #recive roles
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                #verifica la sesion
                verify_jwt_in_request()
                #lo declara como roles
                current_user = get_jwt_identity()
                #jala roles, el current user es un diccionario,  guardando en user roles
                user_roles = json.loads(current_user.get("roles", []))
                #haciendo interseccion entre los 2 roles, si verifica que hay, lo niega     
                if not set(roles).intersection(user_roles):
                    return jsonify({"error": "Acceso no autorizado para este rol"}), 403
                return fn(*args, **kwargs)
            except Exception as e:
                return jsonify({"error": str(e)}), 401

        return wrapper

    return decorator