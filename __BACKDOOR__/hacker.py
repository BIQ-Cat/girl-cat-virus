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
	    break
print("OK")
while True:
	type = input("Is it a query?(y/n): ") == "y"
	if type:
		query = "query|"+input("Enter the command: ")
		s.send(query.encode())
		data = None
		while True:
			data = conn.recv(1024)
			if not data:
			    continue
			break
		print(data)
	else:
		query = "command|"+input("Enter the command: ")
		s.send(query.encode())
		if query.split("|")[1] == "exit":
			s.close()
			break