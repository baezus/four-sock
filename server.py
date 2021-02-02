import socket #import socket module
import hashlib

sha1 = hashlib.sha1()

port = 2345
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print(f'Server listening...on port {port}')

while True:
    conn, addr = s.accept()
    print(f'Got connection from {addr}')
    data = conn.recv(1024)
    print('Server received', data.decode())
    filename="example.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        l = f.read(1024)
    f.close()
    sha1.update(l)
    conn.send(sha1.hexdigest().encode())
    conn.send('     '.encode())
    conn.send(filename.encode())
    print(f'Done sending {filename}.')
    conn.close()