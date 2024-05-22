from flask import render_template
from flask_login import current_user

def list_animals(animals):
    return render_template(
        "animals.html",
        animals=animals,
        title="Lista de animales",
        current_user=current_user,
    )
    
def create_animal():
    return render_template(
        "create_animal.html", title="Crear Animal", current_user=current_user
    )

def update_animal(animal):
    return render_template(
        "update_animal.html",
        title="Editar Animal",
        anima=animal,
        current_user=current_user,
    )