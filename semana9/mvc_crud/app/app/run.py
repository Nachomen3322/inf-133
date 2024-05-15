#definimos como va coexistir/ donde va vivir, su casa
from flask import Flask
#Importa la base de datos, y solo aqui puede estar la bd porque se levanta el servidor
from controllers import user_controller
#importamos la bd
from database import db


#app es un objeto que vivira aqui su casita
app = Flask(__name__)
#Configuracion de base de datos, si o si tiene que tener ese nombre, no se puede llamar otra cosa, y vive en esa ruta sqt.//f
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#hace que no se va trakear las modificacion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Inicializa db con la aplicacion Flask, el contexto es server flask, la app jala el nombre y desactiva el tack modificacion lo de arriba
db.init_app(app)
#Registra el Blueprint de usuarios, aca se registra todos los controladores, este controlador tiene mis rutas GET POST, 
app.register_blueprint(user_controller.user_bp)

#LEVANTANDO EL SERVER

if __name__ == '__main__':
    #cre las tablas si no existen, los crea si no existe
    with app.app_context():
        db.create_all()
    #Debus es modo de testeo
    app.run(debug=True)


#se modifica modelos, vista, html