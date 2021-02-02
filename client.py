import socket
import sys
import argparse
import pickle 

#Creating CLI options and arguments
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
                    metavar="algorithm",
                    action="store",
                    type=str, 
                    choices=["sha1", "sha256", "sha512", "md5"],
                    help="The hashing algorithm to use." 
                    )
parser.add_argument('files',
                    metavar="files",
                    action="store",
                    nargs=argparse.REMAINDER,
                    help="The files to be hashed."
                    )
args = parser.parse_args()

#Getting the socket up and running
s = socket.socket()
host = socket.getfqdn(args.ip)
port = args.port
s.connect((host, port))

#Sending data over the socket

data_packet = [args.algorithm]
for items in args.files:
    data_packet.append(items)
print(data_packet)

pain = str(data_packet)
pain = pain.encode()

s.sendall(pain)

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