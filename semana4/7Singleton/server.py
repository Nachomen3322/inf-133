from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Player:
    _instance = None

    def __new__(cls, name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.health = 100
        return cls._instance

    def to_dict(self):
        return {"name": self.name, "health": self.health}


class PlayerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/player":
            self.send_response(200)
            self.send_header("content-type", "application/json")
            self.end_headers()
            player_data = json.dumps(player_data.to_dict())
            self.wfile.write(player_data.encode("utf-8"))
        else:
            self.send_response(400)
            self.send_headers()

    def do_POST(self):
        if self.path == "/player/damage":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            damage = json.loads(post_data.decode("utf-8"))["damage"]
            player.take_damage(damage)
            self.send_response(201)
            self.end_headers()
            player_data = json.dumps(player.to_dict())
            self.wfile.write(player_data.encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()


def main():
    global player
    player = Player("Alice")

    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, PlayerHandler)
        print("iniciando la malcriada HTTP en el servidor 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando el servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()
