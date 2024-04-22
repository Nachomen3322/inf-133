#render funcion de flask
#Render es una funcion que dice como se va renderizar la pagina, como se va mostrar, con Jinaja2
#Si esta en mayusculas es funcion, si minuscula una
from flask import render_template


#Esto solo renderiza
def usuarios(users):
    #Por eso es importante template, ahi buscara el usuarios.html
    return render_template('usuarios.html', users=users)

#Renderiza registro, devuelve el render template
def registro():
    #En el registro no recibe nada, por eso no mandamos nada, como el users=users ahi si re recibe algo
    return render_template('registro.html')

