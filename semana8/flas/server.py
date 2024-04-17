# importa la clase flask del paquete flask
from flask import Flask, request, jsonify

# jsonify convierte en un kson alfa


# esta clase levanta el httpserver, yano escribir esa uevada, ahi en flask esta el HTTP SERVER, ahi vive
app = Flask(__name__)


# Defiiendo la ruta, por defecto siempre sera get esto. el @ es un decorador (algo con porederes especiales), en este enruta,ya no habra que hacer el doget doPost, et, poder de asociar esa ruta a esa funcion
#
# #lo que esta a '/', asocia a esa funcion, si hay 8 veces solo asociara la ultima creada, por defecto es GETc


@app.route("/")
def hello_world():
    return "Hola, Mundo"


# Construyendo nueva ruta, asociada a la funcion saludar, cuando le agan peticion , se ejecutara saludar
# asocia ruta a funcion el decorador, no es necesario que se llames igual
@app.route("/saludar", methods=["GET"])
def saludar():
    # de request de la tura los obtiene, es un diccionario lo que hay ahi, y se llamara nombre
    nombre = request.args.get("nombres")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parametros de la URL,"}),
            400,
        )
    return jsonify({"Message": f"Hola: {nombre}"})


# SUMA
@app.route("/suma", methods=["GET"])
def sumar():
    num1 = request.args.get("num1")
    num2 = request.args.get("num2")
    if not num1 or not num2:
        return (
            jsonify({"error": "Se requiere dos datos en los parametros de la URL,,"}),
            400,
        )
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    return jsonify({"Message": f"Suma: {num1+num2}"})


# PALINDROMO
@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena = request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere un dato del parametro de la URL,,"}),
            400,
        )
    elif cadena != cadena[::-1]:
        return jsonify({"Message": f"La cadena: {cadena} no es palindromo"})
    return jsonify({"Message": f"La cadena: {cadena} si es palindromo"})


# vocales
@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")
    print(cadena)

    if not cadena or not vocal:
        return (
            jsonify({"error": "Se requiere un dato del parametro de la URL,,"}),
            400,
        )
    contar = cadena.count(vocal)
    return jsonify({"Message": f"La cadena: {cadena} tiene {contar} vocales {vocal}"})


# Le decimos al script como se va levantar
##por defecto tiene puerto 5000
if __name__ == "__main__":
    app.run()
