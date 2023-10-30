import socket
import hashlib

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
            if str_data == "quit" or str_data == "exit":
                break
            print("Client messenge: " + str_data)
            str_data = str_data.replace("client", "server")
            socket_client.send(str_data.encode())
    finally:
        print("Connect Error!!!")
        socket_client.close()

socket_server.close()
