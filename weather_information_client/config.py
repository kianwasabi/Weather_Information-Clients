import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))
hostIP = s.getsockname()[0]
port = 8080
#server_ip = "192.168.178.62:8080" #Broi
server_ip = "192.168.0.228:8080"