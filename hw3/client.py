# Sooji Kim
# CS5700 Fall25
# HW 3: Add 100
# 9 September 2025

#Client program to send data to a server via a socket, and then have that same data echoed back.
import socket

HOST = "127.0.0.1" #The server's host name or IP address
PORT = 65432 #The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Create a new socket using the given address family, socket
    #type and protocol number
    s.connect((HOST, PORT)) #Connect to a remote socket at the address and port
    s.sendall(b"Hello networking!") #Send data to the socket. The socket must be connected to a remote socket. Data type
    #is byte
    data = s.recv(1024) #Receive data from the socket. The return type is a bytes object representing the data received.
    #The maximum amount of data to be received in each chunk is 1024 as specified.
    print(f"Received {data!r}") #print to console