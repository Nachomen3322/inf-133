from flask import Flask
from flask_login import LoginManager
from controllers import user_controller
from controllers import animal_controller
from database import db
from models.user_model import User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zoo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "clave-secreta"
login_manager = LoginManager()
login_manager.login_view = "user.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_uer(user_id):
    return User.query.get(int(user_id))

db.init_app(app)
app.register_blueprint(user_controller.user_bp)
app.register_blueprint(animal_controller.animal_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
