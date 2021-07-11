import socket
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.settimeout(2)
host = input("Host scan:")
port = int(input("Port scan"))

def portscan(port):
    if socket.connect_ex((host.post)):
        print ("Port %d is close :" % (port))
    else: 
         print ("Port %d is open :" % (port))
portscan(port)

#  AF_UNIX liên kết với nút hệ thống tệp được biểu diễn dưới dạng chuỗi
# Các hằng số này đại diện cho các loại socket, được sử dụng cho đối số thứ hai của socket (). Có thể có nhiều hằng số hơn tùy thuộc vào hệ thống. (Chỉ SOCK_STREAM và SOCK_DGRAM có vẻ hữu ích.)