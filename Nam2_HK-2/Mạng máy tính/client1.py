import socket
import hashlib

host = "127.0.0.1"
port = 13337

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((host, port))

msg = "Hello, I am HuyTT-B20DCAT087 client."
print("Client: ", msg)
socket_client.sendall(bytes(msg, "utf8"))
data = socket_client.recv(1024)
print("Server: ", data.decode())

# Thong diep khac lan sau
try:
    while True:
        msg = input("Client: ")
        socket_client.sendall(bytes(msg, "utf8"))
        if msg == "quit" or msg == "exit":
            # ngat ket noi
            break
        data = socket_client.recv(1024)
        print("Server: ", data.decode("utf8"))
finally:
    socket_client.close()
