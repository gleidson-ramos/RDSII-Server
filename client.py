import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall (str.encode('Testando o Servidor'))
data = s.recv(1024)
print('Mensagem: ', data.decode())