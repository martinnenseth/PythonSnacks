import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5000))
s.sendall(('GET / HTTP/1.1\n\n').encode())

print(s.recv(4096))

s.close()