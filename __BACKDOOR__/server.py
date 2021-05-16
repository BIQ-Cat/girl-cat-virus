import socket as sock
import keyboard
import sys
s = sock.socket()
s.bind(('', 9090))
s.listen(1000)
wait = []
while True:
    keyboard.add_hotkey("ctrl+d", lambda: sys.exit(1))
    conn, addr = s.accept()
    data = conn.recv(1024)
    data = data.decode()
    add = data.split("|")
    print(add)
    sucsess = False
    for i, list in enumerate(wait):
        if list[1] == add[1]:
            conn.send(b'200')
            list[2].send(b'200')
            wait[i] = None
            sucsess = True
            break
    if not sucsess:
        add.append(conn)
        wait.append(add)
        print(wait)
