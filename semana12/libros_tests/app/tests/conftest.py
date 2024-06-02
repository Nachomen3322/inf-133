import pytest
from flask_jwt_extended import create_access_token

from database import db
from run import app


@pytest.fixture(scope="module")
def test_client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["JWT_SECRET_KEY"] = "test_secret_key"

    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()


# @pytest.fixture(scope="module")
# def auth_headers():
#     with app.app_context():
#         access_token = create_access_token(
#             identity={"username": "testuser", "roles": '["admin"]'}
#         )
#         headers = {"Authorization": f"Bearer {access_token}"}
#         return headers
    
    
@pytest.fixture(scope="module")
def auth_headers2():
    with app.app_context():
        access_token = create_access_token(
            identity={"username": "tester", "roles": '["user"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}
        return headers
    