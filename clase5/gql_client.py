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

query2 = """
    {
        estudiante(nombre: Jose, apellido: Lopez){
            nombre
            apellido
        }
    }
"""
