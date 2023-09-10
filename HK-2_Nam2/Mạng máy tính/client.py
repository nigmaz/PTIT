import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",1337))
num=input("Enter 2 number: ")
sock.send(num.encode()) #gửi dữ liệu đã được encode
rp=sock.recv(1024)
print(rp.decode())
sock.close()
