#!/usr/bin/env python3
"""
    Implementation of SERVER A
        SEVER A -> Listining IP (Default) - 127.0.0.1 PORT -  55555
        SERVER B -> Listining IP (Default) - 127.0.0.1 PORT - 55556

        on a client request SEVER A will create a thread which will do following task
            Request for Directory Status of server_b on  SERVER B
            Collect Directory Status from server_a on SERVER A
            Combine and Transform Result (such that sort data based
            on filename and will contain only required fields)
            Return Response to client
"""
import threading
# to use multithreading to access multiple clients
import socket
# To create a SERVER A socket to listen client requests
import os
# To access files and directories
import json
# To process bytes data
from myutils import get_list
# custom module to get list of files from a directory

MAX_BYTES_SIZE = 2048

SERVER_B_DIR = os.path.join(os.getcwd(), "server_b_dir")
# Directory path on SERVER B to list data

SERVER_B_IP = "127.0.0.1"
SERVER_B_PORT = 55556

class SERVER:
    """
        Implementation of Server A
    """
    def __init__(self):
        """Default Parameters"""
        self.initlize()

    def initlize(self):
        """initlize server socket"""
        self.socket = socket.socket()
        # creating a server socket
        self.socket.bind((SERVER_B_IP, SERVER_B_PORT))
        # binding server socket to SERVER A's IP and Port
        self.socket.listen()
        temp = "INFO    SERVER B is Ready to Handle Client Request"
        temp += f"at {SERVER_B_IP}:{SERVER_B_PORT}"
        print(temp)
        # SERVER A is ready to Listen Clients

    @staticmethod
    def process_request(csocket, client_ip, client_port):
        """
        method which will do all work as follow
            first it will connect to SERVER_B and access files from SERVER B
        """
        files = get_list(SERVER_B_DIR)
        csocket.send(json.dumps(files).encode())
        client_socket.close()
        print(f"SUCCESS  Data has been sent to client {client_ip}:{client_port}")


if __name__ == "__main__":
    server_socket = SERVER()
    while True:
        client_socket, (cip, cport) = server_socket.socket.accept()
        print(f"INFO    Got a Request from Client {cip}:{cport}")
        thread = threading.Thread(
            target=server_socket.process_request,
            args=[client_socket, cip, cport])
        thread.start()
