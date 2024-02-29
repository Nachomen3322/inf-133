from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#Tiene diccionarios

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Garcia",
        "carrera": "Ingenieria de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Pucas",
        "apellido": "Pascales",
        "carrera": "Ingenieria de Sistemas",
    },
    {
        "id": 3,
        "nombre": "Cristian",
        "apellido": "Sandoval",
        "carrera": "Ingenieria Civil",
    },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/lista_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode('utf-8')) #manda el cuerpo de la respuesta
        #BUSCAR NOMBRE P
        elif self.path == '/buscar_nombre':
            nombres_con_p = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(nombres_con_p).encode('utf-8'))
        #Cantidad de estudiantes por carrera
        elif self.path == '/contar_carreras':
            conteo_carreras = {}
            for estudiante in estudiantes:
                carrera = estudiante["carrera"]
                conteo_carreras[carrera] = conteo_carreras.get(carrera, 0) + 1
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(conteo_carreras).encode('utf-8'))
        #Cantidad total de estudiantes
        elif self.path == '/total_estudiantes':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(len(estudiantes)).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            #los headers son standars
            self.end_headers()
            #hay que convertir a json porque  asi entiende el programa, usamos utf9 para los caracteres de español
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))
            
    def do_POST(self):
        if self.path == '/agrega_estudiante':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            #nos permite convertir cualquier texto plano en un json y de ahi a un diccionario
            post_data = json.loads(post_data.decode('utf-8'))
            #modificamos la cola longitud del array, ya que agregamos uno nuevo
            post_data['id'] = len(estudiantes) + 1
            #agrega, tambien id
            estudiantes.append(post_data)
            #el valor se posteo de manera correcta
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps().encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode('utf-8'))

        
            
def run_server(port = 8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f'Iniciando servidor web en http://localhost:{port}/')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Apagando servidor web')
        httpd.socket.close()

if __name__ == "__main__":
    run_server()