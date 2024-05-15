from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("antes de llamar la funcion")
        result = func(*args, **kwargs).upper()
        print("despues de llamar a la funcion")
        return result
    return wrapper


@my_decorator
def greet(name):
    """Funcion para saludar a alguien"""
    
    print(f"Hola", {name})
    return (name)


greet("Leo")

#aca se ejecuta la funcion
print(greet.__name__)

print(greet.__doc__)
