
def test_get_libros(test_client, auth_headers):
    response = test_client.get("/api/libros", headers=auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro(test_client, auth_headers):
    data = {"titulo": "5AM", "autor": "Robin Sharma", "edicion": 5, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    assert response.json["titulo"] == "5AM"


def test_get_libro(test_client, auth_headers):
    data = {"titulo": "5AM", "autor": "Robin", "edicion": 5, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 200
    assert response.json["titulo"] == "5AM"



def test_update_libro(test_client, auth_headers):
    data = {"titulo": "ONE FACT", "autor": "Kevin de Bruyne", "edicion": 2, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    update_data = {"titulo": "ONE FACT", "autor": "Kevin de Bruyne", "edicion": 2, "disponibilidad" : True}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=auth_headers
    )

    assert response.status_code == 200
    assert response.json["autor"] == "Kevin de Bruyne"
    assert response.json["edicion"] == 2


def test_delete_libro(test_client, auth_headers):
    data = {"titulo": "111", "autor": "222", "edicion": 2, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.delete(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 204

    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers)
    assert response.status_code == 404
    
    
    
    
    
    
    
    
    
    
def test_get_libros2(test_client, auth_headers2):
    response = test_client.get("/api/libros", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json == []


def test_create_libro2(test_client, auth_headers2):
    data = {"titulo": "5AM", "autor": "Robin Sharma", "edicion": 5, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers2)
    assert response.status_code == 201
    assert response.json["titulo"] == "5AM"


def test_get_libro2(test_client, auth_headers2):
    data = {"titulo": "6AM", "autor": "Robin", "edicion": 5, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers2)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 200
    assert response.json["titulo"] == "5AM"


def test_update_libro2(test_client, auth_headers2):
    data = {"titulo": "ONE FACT", "autor": "Kevin de Bruyne", "edicion": 2, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers2)
    assert response.status_code == 201
    libro_id = response.json["id"]

    update_data = {"titulo": "ONE FACT", "autor": "Kevin de Bruyne", "edicion": 2, "disponibilidad" : True}
    response = test_client.put(
        f"/api/libros/{libro_id}", json=update_data, headers=auth_headers2
    )

    assert response.status_code == 200
    assert response.json["autor"] == "Kevin de Bruyne"
    assert response.json["edicion"] == 2


def test_delete_libro2(test_client, auth_headers2):
    data = {"titulo": "111", "autor": "222", "edicion": 2, "disponibilidad" : True}
    response = test_client.post("/api/libros", json=data, headers=auth_headers2)
    assert response.status_code == 201
    libro_id = response.json["id"]

    response = test_client.delete(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 204

    response = test_client.get(f"/api/libros/{libro_id}", headers=auth_headers2)
    assert response.status_code == 404
    


