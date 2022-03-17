import socket

target = input("Domain or IP to scan: ")
open_ports = []

for i in range(78, 85):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if sock.connect_ex((target, i)) == 0:
        open_ports.append(i)

    sock.close() 
        
[print(f"Port {x} is open") for x in open_ports]

