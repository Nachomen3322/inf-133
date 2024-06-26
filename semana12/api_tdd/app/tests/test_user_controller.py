import pytest
from models.user_model import User


@pytest.fixture
def new_user():
    return{"username":"testuser", "password":"testpassword"}

#lo primo que hacemos es registrar user, luego el login

#debe indicar que son los tests, por esto es implicito
def test_register_user(test_client, new_user):
    #mandando a la ruta api/register ya que ahi se construye, diciendo que es post enviamos . Por defecto se creara un user, no admin
    response = test_client.post("/api/register", json=new_user)
    #en que casos se creara si el username no tiene otro username igual, si no cumple, el assert te da red point
    assert response.status_code == 201
    assert response.json["message"] == "Usuario creado exitosamente"


#es un test de usuario duplicado
def test_register_duplicate_user(test_client, new_user):
    #verificamos si se puede registar, pero no deberia porque ya existe
    response = test_client.post("/api/register", json=new_user)
    #error
    assert response.status_code == 400
    #tiene que haber este mensaje, SI SALE 200 ENTONCES SE ESTA DUPLICANDO EL USER Y NO DEBERIA CAPAR
    assert response.json["error"] == "El nombre de usuario ya está en uso"


#Prueba de el login
def test_login_user(test_client, new_user):
    #tenemos credenciales
    #hacemos login con el user, si sus credenciales son correctas todo deberia ir bien
    #200 = pudiste logearte OK
    login_credentials = {
        "username": new_user["username"],
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 200
    assert response.json["access_token"]
    
def test_login_invalid_user(test_client, new_user):
    #se intenta iniciar sesion sin registrar al usuario
    login_credentials = {
        "username": new_user["username"],
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credentiales invalidas"
    
def test_login_wrong_password(test_client, new_user):
    #se intenta iniciar sesion con contraseña incorrecta
    login_credentials = {
        "username": new_user["username"],
        "password": new_user["wrongpassword"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    assert response.status_code == 401
    assert response.json["error"] == "Credentiales invalidas"