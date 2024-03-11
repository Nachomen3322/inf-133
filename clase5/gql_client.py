import requests

# Definir la consulta GraphQL
query = """
    {
        estudiante(id: 2, nombre: "Jose Dir"){
            nombre
        }
    }
"""

# Defininedo la url del servidor GraphQL
url = "http://localhost:8000/graphql"

# Solicitando POST al servidor GQL
response = requests.post(url, json={"query": query})
print(response.text)
