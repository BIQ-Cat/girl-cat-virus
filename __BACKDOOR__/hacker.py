import socket as sock
import sys
s = sock.socket()
s.connect(('localhost', 9090))
id = input("Print ID: ")
query = "hacker|"+id
print(query)
s.send(query.encode())
while True:
    data = s.recv(1024)
    if not data:
        continue
    if data != b'200':
        s.close()
        sys.exit(1)
    if data == b'200':
        s.close()
        break
print("OK")