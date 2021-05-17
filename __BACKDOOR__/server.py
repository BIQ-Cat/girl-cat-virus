import socket as sock
import threading
import sys
s = sock.socket()
s.bind(('', 9090))
s.listen(1000)
wait = []
def remote(hacker, client):
    while True:
        data = hacker.recv(2048)
        if not data:
            continue
        client.send(data)
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    data = data.decode()
    add = data.split("|")
    print(add)
    sucsess = False
    for i, lst in enumerate(wait):
        if lst[1] == add[1]:
            conn.send(b'200')
            lst[2].send(b'200')
            if add == "hacker":
                th = threading.Thread(target=remote, args=(conn, lst[2],))
            else:
                th = threading.Thread(target=remote, args=(lst[2], conn,))
            th.start()
            sucsess = True
            break
    if not sucsess:
        add.append(conn)
        wait.append(add)
        print(wait)
