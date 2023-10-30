import socket
from hashlib import *

key = "httb20at087"
host = "127.0.0.1"
port = 13337

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen(10)  # vao tran thai listen, chap nhan toi da 10 client

while True:
    socket_client, addr = socket_server.accept()
    try:
        print("Connected by", addr)
        while True:
            msg = socket_client.recv(1024)
            str_data = msg.decode()
            print("Client messenge: " + str_data)
            # check hash
            Hash_client = socket_client.recv(1024).decode()
            if (
                Hash_client
                != sha512(str_data.encode("utf8") + key.encode("utf8")).hexdigest()
            ):
                print("The received messenge has lost it's integrity.")
                str_data = "The received messenge has lost it's integrity."
                socket_client.send(str_data.encode())
            else:
                if str_data == "quit" or str_data == "exit":
                    break
                str_data = str_data.replace("client", "server")
                socket_client.send(str_data.encode())
    finally:
        print("Connect Error!!!")
        socket_client.close()

socket_server.close()
