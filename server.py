import socket #import socket module
import hashlib


port = 2345
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print(f'Server listening...on port {port}')

while True:
    conn, addr = s.accept()
    print(f'Got connection from {addr}')
    data = conn.recv(4096)
    data = data.decode('utf-8')
    data = eval(data)

    print('Server received', data)
    if "sha1".encode() in data:
        parser = hashlib.sha1()
        print('sha1 in data decode')
    elif "sha256".encode() in data:
        parser = hashlib.sha256()
        print('sha256 in data decode')
    elif "sha512".encode() in data:
        parser = hashlib.sha512()
        print('sha512 in data decode')
    elif "md5".encode() in data:
        parser = hashlib.md5()
        print('md5 in data decode')
    
    filename = "example.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        l = f.read(1024)
        conn.send(parser(l).hexdigest())
    f.close()
    result = parser(l).hexdigest()

    # conn.send(result.encode())
    conn.send('     '.encode())
    conn.send(filename.encode())
    print(f'Done sending {filename}.')
    conn.close()

    # filename="example.txt"
    # f = open(filename, 'rb')
    # l = f.read(1024)
    # while (l):
    #     l = f.read(1024)
    # f.close()
    # sha1.update(l)
    # conn.send(sha1.hexdigest().encode())
    # conn.send('     '.encode())
    # conn.send(filename.encode())
    # print(f'Done sending {filename}.')
    # conn.close()