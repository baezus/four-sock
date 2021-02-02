import socket #import socket module
import hashlib

sha256 = hashlib.sha256()

port = 2346
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print(f'Server listening...on port {port}')

while True:
    conn, addr = s.accept()
    print(f'Got connection from {addr}')
    data = conn.recv(1024)
    print('Server received', repr(data))
    filename="example.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        l = f.read(1024)
    sha256.update(l)
    conn.send(sha256.hexdigest().encode())
    f.close()

    print(f'Done sending {filename}.')
    conn.close()