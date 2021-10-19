#!/usr/bin/env python3
"""
    client socket implementation which
        client will send a request to SERVER A
        client will Recv files list from SERVER A
        client will print files data on output
"""
import socket
# To create and manipulate sockets
import json
# To Serialize and Deserialize Objects

SERVER_A_IP = "127.0.0.1"
SERVER_A_PORT = 55555
MAX_BYTES_SIZE = 2048

if __name__ == "__main__":
    client_socket = socket.socket()
    client_socket.connect((SERVER_A_IP, SERVER_A_PORT))
    files = json.loads(client_socket.recv(MAX_BYTES_SIZE))
    LENGTH = 0
    for item in files:
        for attr in item:
            if len(attr) > LENGTH:
                LENGTH = len(attr)
    for name, size, mtime in files:
        print(f"{name:<{LENGTH}} {size:^{LENGTH}} {mtime:^{LENGTH}}")

    client_socket.close()
