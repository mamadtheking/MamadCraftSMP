from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
import os

HOST = "mamadcraftsmp.aternos.me"
PORT = 25565


def check_server():
    try:
        ip = socket.gethostbyname(HOST)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((ip, PORT))
        sock.close()

        return {
            "online": result == 0,
            "players": 0,
            "max_players": 0
        }

    except Exception:
        return {
            "online": False,
            "players": 0,
            "max_players": 0
        }


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/status":
            data = check_server()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())

        else:
            self.send_response(404)
            self.end_headers()


port = int(os.environ.get("PORT", 5000))

server = HTTPServer(("0.0.0.0", port), Handler)

print("Mamad Craft Backend started!")

server.serve_forever()
