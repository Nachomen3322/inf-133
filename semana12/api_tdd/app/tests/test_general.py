#ESTE LO QUE recibe es un cliente del conftest
def test_index(test_client):
    #que haga el cliente un get a index, y lo guarde en response, ahi se almacenara el status code, el cuerpo de solicitus, de respuesta
    response = test_client.get("/")
    #asser = comparacion logica, que si el status code sea igual y que sea true, si es true = salio bien, si no mal
    assert response.status_code == 404


#verificando que se levante el swagger, recibe al cliente de prueba
def test_swagger_ui(test_client):
    #hace un get a api/docs
    response = test_client.get("/api/docs/")
    #si todo esta bien, verificamos con el assert, y esta OK
    assert response.status_code == 200
    #necesitamos estar seguro que la pagina que se devuelva es el swagger, con esto verificamos, la respuesta sera un html, por eso la "b" adelante para que se enteere
    assert b'id="swagger-ui"' in response.data
    #puedes seguir agregando mas cosas