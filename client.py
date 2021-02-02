import socket
import sys
import argparse 

parser = argparse.ArgumentParser(description="A network hashing server implementing sha1, sha256, sha512, and md5.")
parser.add_argument("-port",
                    metavar="port",
                    type=int,
                    action="store",
                    default="2345",
                    help="The port to access.")
parser.add_argument("ip",
                    metavar="ip",
                    action="store",
                    default="127.0.1.1",
                    help="The IP domain to network on.")
parser.add_argument('algorithm', 
                    action="store",
                    type=str, 
                    choices=["sha1", "sha256", "sha512", "md5"],
                    help="The hashing algorithm to use." 
                    )
parser.add_argument('files',
                    action="store",
                    nargs=argparse.REMAINDER,
                    help="The files to be hashed."
                    )
args = parser.parse_args()

s = socket.socket()
host = socket.getfqdn(args.ip)
port = args.port

s.connect((host, port))
s.send('Hello server!'.encode())

with open('clientside_file', 'wb') as f:
    print(f'Connecting to {args.ip}:{port}')
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

f.close()
s.close()

with open('clientside_file', 'r') as fin:
  print(fin.read())
# print(vars(args))