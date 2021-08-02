import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('ip_address',21))

msg = s.recv(2048).decode()
print(msg)

s.close()
