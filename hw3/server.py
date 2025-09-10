# Sooji Kim
# CS5700 Fall25
# HW 3: Add 100
# 9 September 2025

#A simple program that will create a server that echos a client request back to the client.

import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            num = int(data.decode())
            num += 100
            # convert int to bytes and return to client
            conn.sendall(str(num).encode())