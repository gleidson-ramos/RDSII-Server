import socket

HOST = 'localhost'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print('Aguardando')
conn, ender = s.accept()

print ('conectado: ' ,ender)
while True:
    data = conn.recv(1024)
    if not data:
        print('fechando')
        conn.close()
        break

    conn.sendall (data)