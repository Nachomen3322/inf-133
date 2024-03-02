import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# DELETE elimina todos los estudiantes por la ruta /estudiantes
# ruta_eliminar = url + "estudiantes"
# eliminar_response = requests.request(method="DELETE",
#                                     url=ruta_eliminar)
# print(eliminar_response.text)

# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Perez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET busca a un estudiante por id /estudiantes/{id}
# despues puede haber una barra, nombre, etc.
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)

# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "estudiantes"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, json=estudiante_actualizado
)
print(put_response.text)


# Tarea
# Muestra todas las carreras
print("------------------MOSTRAR TODAS LAS CARRERAS-----------------------")
ruta_getCarreras = url + "carreras"
get_responseCarerra = requests.request(method="GET", url=ruta_getCarreras)
print(get_responseCarerra.text)


# GET devuelve a los estudiantes de la carrera de "Economia"
print("------------------MOSTRAR ESTUDIANTE DE ECONOMIA-----------------------")
ruta_filtrar_carrera = url + "Economia"
filtrar_carrera_response = requests.request(method="GET", url=ruta_filtrar_carrera)
print(filtrar_carrera_response.text)


# Post para agregar 2 nuevos estudiantes de la carrera de Economía
ruta_post = url + "estudiantes"
nuevo_estudiante1 = {"nombre": "Tyler", "apellido": "Joseph", "carrera": "Bellas Artes"}
nuevo_estudiante2 = {
    "nombre": "",
    "apellido": "Perez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingenieria",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
