from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema


class Estudiante(ObjectType):
    id = Int()
    nombre = String()
    apellido = String()
    carrera = String()


estudiantes = [
    Estudiante(id=1, nombre="Andrea", apellido="Granados", carrera="Bellas Artes"),
    Estudiante(id=2, nombre="Lionel", apellido="Messi", carrera="Ingenieria Civil"),
]


class Query(ObjectType):
    estudiantes = List(Estudiante)

    def resolve_estudiantes(root, info):
        print(estudiantes)
        return estudiantes
