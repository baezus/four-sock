import socket #import socket module
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
    print('Server received', repr(data))
    filename="example.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print('Sent ', repr(l))
        l = f.read(1024)
    f.close()

    print(f'Done sending {filename}.')
    conn.send('Thank you for connecting!'.encode())
    conn.close()