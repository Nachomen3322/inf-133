def render_user_list(users):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": user.id,
            "username": user.username,
            "password": user.password,
            "roles": user.roles,
        }
        for user in users
    ]


def render_user_detail(user):
    # Representa los detalles de un animal como un diccionario
    return {
        "id": user.id,
        "username": user.username,
        "password": user.password,
        "roles": user.roles,
    }
