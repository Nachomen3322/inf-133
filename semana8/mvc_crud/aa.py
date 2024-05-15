# # El Jina se usa con python y sus frameworkds, dentro de

# # variables en Jina


# # el {{title}} esa es la variable. Esa variable se envia al template/pagina, asi se define la variable


# # como se envia desde la vista


# #asi se manda las variables
# def registro():
#     return render_template("registro.html", title="Registro de Usuarios")

# #puedes agarrar variabes de un buvle, de un if, etc

# #users para el bucle for, el title para la etiqueta 
# def registro():
#     return render_template("registro.html", users=users ,title="Registro de Usuarios", )


# #se puede ejecutar codigos de python en un html, este por ejm lo poner todo mayuscula
# #
# <nav>
#     <a href="/"> {{title.uper() }} </a>
# <nav>

# ## busca e bñurpirint que se llama users, y asi se emrita ñas ágomas  y servicios creados dentro del cotrolador


# #bloque mutados/sobreescritura, nos permite definir un espacio donde podemos hacer lo que quieras
# #el blqoeute tiene dos partes, el incio 
# <div>
#     (% block content %)(% endblock %)
# </div>


# #Existe herencia en plantillas, se utiliza la notacion (%extends 'base.html' %), hereda todo de base.html a usuario..htm actual file
# #La herencia siempre al principio



# #EN EL FOR el user no pueden enviarlo, es local, el users si viene de afuera

# #flujos de control, puedes usar if else endif, lo mismo que python, el age hay que enviarle age mas para que lo utiliza


