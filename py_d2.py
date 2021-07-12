import socket
from termcolor import colored;
socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.settimeout(1)
host = input("Host scan:")
# port = int(input("Port scan"))

def portscan(port):
    if socket.connect_ex((host.post)):
        print (colored("Port %d is close :" %(port), 'red'))
    else: 
         print ("Port %d is open :" % port)
for port in range(1,10):
        portscan(port)
