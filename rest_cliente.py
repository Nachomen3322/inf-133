import requests

url = "http://localhost:8000/"
# GET consulta a la ruta /lista_estudiantes
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Lerez",
    "carrera": "Ingenieria Agronomica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

print("------------------------------------------------------------------------")

#BUSCAR NOMBRE
ruta_getP = url + "buscar_nombre"
get_responseP = requests.request(method="GET", url=ruta_getP)
print(get_responseP.text)

#CONTEO CARRERAS
print("------------------------------------------------------------------------")
ruta_getConteo = url + "contar_carreras"
get_responseConteo = requests.request(method="GET", url=ruta_getConteo)
print(get_responseConteo.text)

#Cantidad total
print("------------------------------------------------------------------------")
ruta_getContarEst = url + "total_estudiantes"
get_responseConteoEst = requests.request(method="GET", url=ruta_getContarEst)
print("Cantidad de estudiantes:", get_responseConteoEst.text)


