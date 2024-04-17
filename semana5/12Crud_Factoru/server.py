from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de vehículos
vehicles = {}

class DeliveryVehicle:
    def __init__(self, vehicle_type, plate_number, capacity):
        self.vehicle_type = vehicle_type
        self.plate_number = plate_number
        self.capacity = capacity

class Motorcycle(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("motorcycle", plate_number, capacity)


class Drone(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("drone", plate_number, capacity)


class DeliveryFactory:
    @staticmethod
    def create_vehicle(vehicle_type, plate_number, capacity):
        if vehicle_type == "drone":
            return Drone(plate_number, capacity)
        elif vehicle_type == "motorcycle":
            return Motorcycle(plate_number, capacity)
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")

class Motorcycle(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("motorcycle", plate_number, capacity)


class Drone(DeliveryVehicle):
    def __init__(self, plate_number, capacity):
        super().__init__("drone", plate_number, capacity)


class DeliveryFactory:
    @staticmethod
    def create_vehicle(vehicle_type, plate_number, capacity):
        if vehicle_type == "drone":
            return Drone(plate_number, capacity)
        elif vehicle_type == "motorcycle":
            return Motorcycle(plate_number, capacity)
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")
class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))
    
