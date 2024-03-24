import requests

# Definir la consulta GraphQL
query = """
    {
        estudiante(id: 1){
            nombre
            apellido
            carrera
        }
    }
"""

# Definir la URL del servidor GraphQL
url = "http://localhost:8000/graphql"

# Hacer la solicitud POST al servidor GraphQL
response = requests.post(url, json={"query": query})
print(response.text)

# Definir otra consulta GraphQL
query2 = """
    {
        estudiante(id: 2){
            nombre
            apellido
            carrera
        }
    }
"""

# Hacer otra solicitud POST al servidor GraphQL
response = requests.post(url, json={"query": query2})
print(response.text)

query3 = """
    {
        estudiante(id: 2){
            nombre
            apellido
        }
    }
"""
response = requests.post(url, json={"query": query3})
print(response.text)

query_crear = """
mutation{
        crearEstudiante(nombre: "Messi", apellido: "Sandoval", carrera: "Comunicacion Social") {
            estudiante {
                id  
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={"query": query_crear})
print(response_mutation.text)

crearEstudiante1 = """
mutation {
    crearEstudiante(nombre: "Juan", apellido: "Pérez", carrera: "Arquitectura") {
        estudiante {
            id  
            nombre
            apellido
            carrera
        }
    }
}
"""

crearEstudiante2 = """
mutation {
    crearEstudiante(nombre: "María", apellido: "Gonzalez", carrera: "Arquitectura") {
        estudiante {
            id  
            nombre
            apellido
            carrera
        }
    }
}
"""

crearEstudiante3 = """
mutation {
    crearEstudiante(nombre: "Carlos", apellido: "Martínez", carrera: "Arquitectura") {
        estudiante {
            id  
            nombre
            apellido
            carrera
        }
    }
}
"""
print("RESPUESTA")
response_mutation = requests.post(url, json={"query": crearEstudiante1})
print(response_mutation.text)
response_mutation = requests.post(url, json={"query": crearEstudiante2})
print(response_mutation.text)
response_mutation = requests.post(url, json={"query": crearEstudiante3})
print(response_mutation.text)

query_arquitectura = """
{
    estudiantesPorCarrera(carrera: "Arquitectura") {
        id
        nombre
        apellido
        carrera
    }
}
"""
response_arquitectura = requests.post(url, json={"query": query_arquitectura})
print(response_arquitectura.text)


query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante{
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)
