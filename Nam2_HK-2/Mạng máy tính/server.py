import socket
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tạo đối tượng socket, AF_INET là họ địa chỉ Internet cho IPv4. SOCK_STREAM là giao thức cho TCP.
 
# sock.bind(("localhost", 1337)) # liên kết socket với một giao diện mạng cụ thể và số cổng. Nó sẽ phụ thuộc vào họ địa chỉ ip mà mình kết nối. Ở đây đang sử dụng ipv4 nên sẽ kết nối tới mạng localhost có địa chỉ ip là 127.0.0.1 và cổng 1337
sock.bind(("172.20.10.12", 1337))

sock.listen(1) # cho phép máy chủ chấp nhận kết nối TCP
 
while 1:
    conn, addr = sock.accept() # máy chủ đợi đến khi có các request tiếp theo, trả về socket mới được tạo ra
    res=conn.recv(1024).decode() # đọc kiểu 1024 bytes từ socket
    sp=res.split(" ") # tách chuỗi
    li=list(map(int,sp)) # lưu chuỗi vừa tách vào list dưới dạng int
    if len(li)==2 and li[1]!=0: # nếu độ dài của list = 2 (nhập vào 2 số) và số b khác 0 thì thực hiện phép tính
        ss = li[0]+li[1]
        subt = li[0]-li[1]
        mult = li[0]*li[1]
        div = li[0]/li[1]
        ss = "Tong: "+str(ss)+'\nHieu: '+str(subt)+'\nNhan: '+str(mult)+'\nChia: '+str(div)
    else:
        ss = "Khong hop le"
    print(ss)
    conn.send(ss.encode()) # đọc dữ liệu và gửi lại về server
    conn.close() # đóng kết nối tới client này (nhưng không đóng socket)
    if not res:
        break 
