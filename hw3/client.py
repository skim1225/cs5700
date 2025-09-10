# Sooji Kim
# CS5700 Fall25
# HW 3: Add 100
# 9 September 2025

#Client program to send data to a server via a socket, and then have that same data echoed back.

import socket
import sys

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # get terminal input
    num = int(sys.argv[1])
    # convert input to bytes and send to server
    s.sendall(str(num).encode())
    data = s.recv(1024)
    print(f"Sent {num} and received {data!r}")