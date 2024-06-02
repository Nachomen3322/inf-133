# import requests

# # URL base de la API
# BASE_URL = "http://localhost:5000/api"

# # Definir los encabezados de la solicitud
# headers = {"Content-Type": "application/json"}

# # Crear un nuevo libro
# url = f"{BASE_URL}/libros"
# nuevo_libro = {"titulo": "CLUB 5AM", "autor": "Robin Sharma", "edicion": "7", "disponibilidad": True}
# response = requests.post(url, json=nuevo_libro, headers=headers)
# print("Creando un nuevo libro:")
# print(response.json())

# # Crear el segundo libro
# url = f"{BASE_URL}/libros"
# nuevo_libro = {"titulo": "METAMORFOSIS", "autor": "Franz Kafka", "edicion": "3", "disponibilidad": False}
# response = requests.post(url, json=nuevo_libro, headers=headers)
# print("Creando el segundo libro:")
# print(response.json())

# # Crear el segundo libro
# url = f"{BASE_URL}/libros"
# nuevo_libro = {"titulo": "F*ck that", "autor": "Jason Headley", "edicion": "5", "disponibilidad": True}
# response = requests.post(url, json=nuevo_libro, headers=headers)
# print("Creando el tercer libro:")
# print(response.json())

# # Obtener la lista de todos los libros
# url = f"{BASE_URL}/libros"
# response = requests.get(url, headers=headers)
# print("\nLista de libros:")
# print(response.json())

# # Obtener un libro específico por su ID (por ejemplo, ID=1)
# url = f"{BASE_URL}/libros/1"
# response = requests.get(url, headers=headers)
# print("\nDetalles del libro con ID 1:")
# print(response.json())

# # Actualizar un libro existente por su ID (por ejemplo, ID=1)
# url = f"{BASE_URL}/libros/2"
# datos_actualizacion = {"titulo": "METAMORFOSIS", "autor": "Arramayo Luan", "edicion": "1", "disponibilidad": True}
# response = requests.put(url, json=datos_actualizacion, headers=headers)
# print("\nActualizando el libro con ID 2:")
# print(response.json())

# # Eliminar un libro existente por su ID (por ejemplo, ID=1)
# url = f"{BASE_URL}/libros/1"
# response = requests.delete(url, headers=headers)
# print("\nEliminando el libro con ID 1:")
# if response.status_code == 204:
#     print(f"libro con ID 1 eliminado con éxito.")
# else:
#     print(f"Error: {response.status_code} - {response.text}")