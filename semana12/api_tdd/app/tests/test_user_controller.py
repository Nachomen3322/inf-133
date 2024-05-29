#lo primo que hacemos es registrar user, luego el login

#debe indicar que son los tests, por esto es implicito
def test_register_user(test_client):
    #creamos lo que se va enfiar al server, igual se va matar, 201 = se creo con exito
    new_user = {"username": "testuser", "password": "testpassword"}
    #mandando a la ruta api/register ya que ahi se construye, diciendo que es post enviamos . Por defecto se creara un user, no admin
    response = test_client.post("/api/register", json=new_user)
    #en que casos se creara si el username no tiene otro username igual, si no cumple, el assert te da red point
    assert response.status_code == 201


#es un test de usuario duplicado
def test_register_duplicate_user(test_client):
    new_user = {"username": "testuser", "password": "testpassword"}
    #verificamos si se puede registar, pero no deberia porque ya existe
    response = test_client.post("/api/register", json=new_user)
    #error
    assert response.status_code == 400
    #tiene que haber este mensaje, SI SALE 200 ENTONCES SE ESTA DUPLICANDO EL USER Y NO DEBERIA CAPAR
    assert response.json["error"] == "El nombre de usuario ya está en uso"


#Prueba de el login
def test_login_user(test_client):
    #tenemos credenciales
    user_credentials = {"username": "testuser", "password": "testpassword"}
    #hacemos login con el user, si sus credenciales son correctas todo deberia ir bien
    response = test_client.post("/api/login", json=user_credentials)
    #200 = pudiste logearte OK
    assert response.status_code == 200