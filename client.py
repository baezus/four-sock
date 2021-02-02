import socket
import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("-p port",
                    action="store",
                    default="2345")
parser.add_argument("ip",
                    action="store",
                    default="127.0.0.1")
parser.add_argument('algorithm', 
                    action="store", 
                    choices=["sha1", "sha256", "sha512", "md5"], 
                    )
parser.add_argument('files',
                    action="store",
                    nargs=argparse.REMAINDER
                    )
args = parser.parse_args()

s = socket.socket()
host = socket.gethostname()
port = 2345
ip = socket.gethostbyname(host)

s.connect((host, port))
s.send('Hello server!'.encode())

with open('clientside_file', 'wb') as f:
    print(f'Connecting to {ip}:{port}')
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

f.close()
s.close()

with open('clientside_file', 'r') as fin:
  print(fin.read())
print(vars(args))