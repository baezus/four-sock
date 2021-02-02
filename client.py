import socket

s = socket.socket()
host = socket.gethostname()
port = 2346

s.connect((host, port))
s.send('Hello server!'.encode())

with open('clientside_file', 'wb') as f:
    print('new file opened on client')
    while True:
        print('receiving data from server...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        #write data to a file
        f.write(data)
f.close()
print('Successfully got the file.')
s.close()
print('connection closed.')