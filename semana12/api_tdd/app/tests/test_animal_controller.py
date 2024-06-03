
# #el auth_headers nos sirve pora el el token, que si tiene puede
# def test_get_animals(test_client, auth_headers):
#     #la lista de todos los animales, el headers = envia el token, 
#     response = test_client.get("/api/animals", headers=auth_headers)
#     #como tiene rol de admin debe dar 200
#     assert response.status_code == 200
#     # si se cumple todo bien
#     assert response.json == []

# #si un test falla, los siguientes siguen creamdose, y al final te da un reporte


# def test_create_animal(test_client, auth_headers):
#     data = {"name": "Lion", "species": "Panthera leo", "age": 5}
#     response = test_client.post("/api/animals", json=data, headers=auth_headers)
#     #deberia poder crear por ser admin
#     assert response.status_code == 201
#     #en el cuerpo de la respuesta debe de haber el Lion, si responde todo bien
#     assert response.json["name"] == "Lion"


# def test_get_animal(test_client, auth_headers):
#     # Primero crea un animal
#     #crea un animal primero, debe exister
#     data = {"name": "Tiger", "species": "Panthera tigris", "age": 3}
#     response = test_client.post("/api/animals", json=data, headers=auth_headers)
    
#     #si esto falla, lo de abajo ya no sigue
#     assert response.status_code == 201
#     animal_id = response.json["id"]

#     # Ahora obtén el animal
#     #obtiene el nombre de un animal en especifico
#     response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
#     assert response.status_code == 200
#     assert response.json["name"] == "Tiger"



# def test_update_animal(test_client, auth_headers):
#     # Primero crea un animal
#     #siempre creando primero al animal
#     data = {"name": "Elephant", "species": "Loxodonta", "age": 10}
#     response = test_client.post("/api/animals", json=data, headers=auth_headers)
#     #verificando si se puede crear
#     assert response.status_code == 201
#     animal_id = response.json["id"]

#     # Ahora actualiza el animal
#     update_data = {"name": "Elephant", "species": "Loxodonta africana", "age": 12}
#     response = test_client.put(
#         f"/api/animals/{animal_id}", json=update_data, headers=auth_headers
#     )
#     #tenemos que veriricar 3 cosas, primero que de 200, despues que los datos no modificados se mantengan
#     assert response.status_code == 200
#     assert response.json["species"] == "Loxodonta africana"
#     assert response.json["age"] == 12


# #LO MISMO
# def test_delete_animal(test_client, auth_headers):
#     # Primero crea un animal
#     data = {"name": "Giraffe", "species": "Giraffa camelopardalis", "age": 7}
#     response = test_client.post("/api/animals", json=data, headers=auth_headers)
#     assert response.status_code == 201
#     animal_id = response.json["id"]

#     # Ahora elimina el animal
#     response = test_client.delete(f"/api/animals/{animal_id}", headers=auth_headers)
#     #exito sin respuesta
#     assert response.status_code == 204

#     # Verifica que el animal ha sido eliminado
#     response = test_client.get(f"/api/animals/{animal_id}", headers=auth_headers)
#     assert response.status_code == 404