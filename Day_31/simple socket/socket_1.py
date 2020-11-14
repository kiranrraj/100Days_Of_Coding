# Title  : Echo server
# Author : Kiran Raj R.
# Date   : 14/11/2020

import socket

HOST = "127.0.0.1"
PORT = 65432

# The arguments passed to socket() specify the address family and 
# socket type. AF_INET is the Internet address family for IPv4. 
# SOCK_STREAM is the socket type for TCP, the protocol that will 
# be used to transport our messages in the network.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)