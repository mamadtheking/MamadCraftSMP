from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socket
import os
import struct

HOST = "mamadcraftsmp.aternos.me"
PORT = 25565


def write_varint(value):
    data = bytearray()

    while True:
        temp = value & 0x7F
        value >>= 7

        if value:
            temp |= 0x80

        data.append(temp)

        if not value:
            break

    return bytes(data)


def read_varint(sock):
    value = 0
    shift = 0

    while True:
        byte = sock.recv(1)

        if not byte:
            raise ConnectionError()

        byte = byte[0]
        value |= (byte & 0x7F) << shift

        if not (byte & 0x80):
            return value

        shift += 7

        if shift > 35:
            raise ValueError("Invalid VarInt")


def check_server():
    try:
        ip = socket.gethostbyname(HOST)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((ip, PORT))

        # Minecraft Handshake
        host_bytes = HOST.encode()

        handshake_data = (
            write_varint(767) +
            write_varint(len(host_bytes)) +
            host_bytes +
            struct.pack(">H", PORT) +
            write_varint(1)
        )

        handshake_packet = (
            write_varint(len(handshake_data) + 1) +
            write_varint(0) +
            handshake_data
        )

        sock.sendall(handshake_packet)

        # Status Request
        sock.sendall(b"\x01\x00")

        # Read response
        packet_length = read_varint(sock)

        packet_data = b""

        while len(packet_data) < packet_length:
            chunk = sock.recv(packet_length - len(packet_data))

            if not chunk:
                raise ConnectionError()

            packet_data += chunk

        # Remove packet ID
        offset = 0

        packet_id = packet_data[offset]
        offset += 1

        # Read JSON length
        json_length = 0
        shift = 0

        while True:
            byte = packet_data[offset]
            offset += 1

            json_length |= (byte & 0x7F) << shift

            if not (byte & 0x80):
                break

            shift += 7

        json_data = packet_data[offset:offset + json_length]

        status = json.loads(json_data.decode("utf-8"))

        players = status.get("players", {})

        online_players = players.get("online", 0)
        max_players = players.get("max", 0)

        sock.close()

        return {
            "online": True,
            "players": online_players,
            "max_players": max_players
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

            self.wfile.write(
                json.dumps(data).encode()
            )

        else:

            self.send_response(404)
            self.end_headers()


port = int(os.environ.get("PORT", 5000))

server = HTTPServer(("0.0.0.0", port), Handler)

print("Mamad Craft Backend started!")

server.serve_forever()
