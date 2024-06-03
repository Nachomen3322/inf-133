import pytest
from flask_jwt_extended import create_access_token

from database import db
from run import app


@pytest.fixture(scope="module")
def test_client():
    #SIEMPRE SERA TRUE
    app.config["TESTING"] = True
    #configurando la base de datos, poniento que sear de memoria y sera temporal, que no se registrara
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    #la key
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    #levantando un cliente de pruena con la funcion test cliente
    with app.test_client() as testing_client:
        #creando bd temoral
        with app.app_context():
            #ejecutando
            db.create_all()
            #el yield = mientras esto este vivo
            yield testing_client
            #lo borra todo
            db.drop_all()


#SIMULANDO LOS TOKENS, el pytest = esta funcion se debe ejecutar con los pytest cuando se ejecuta pytest
@pytest.fixture(scope="module")
#esta funcion basicamente genera tokens, solo funcionara para admin, si para que funciona a otro envez de admin, user o los dos roles
def admin_auth_headers():
    #si existe servidor de prueba, crea token
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        #construye cabezera donde estara el token
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
    
    
@pytest.fixture(scope="module")
def user_auth_headers():
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "user", "roles": '["user"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers  