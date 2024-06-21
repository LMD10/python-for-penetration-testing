# python-for-penetration-testing
Welcome to the "Python for Penetration Testing" repository! This collection features scripts and tools developed using Python to enhance and automate various tasks in the penetration testing lifecycle. These projects complement my formal education at the University of Manchester and showcase my skills and knowledge in cybersecurity and programming.

Introduction
This repository contains a series of Python scripts designed to assist in penetration testing tasks, such as network scanning, port scanning, and service enumeration. These tools demonstrate practical applications of network sockets and interaction with network services, providing a foundation for more advanced security assessments.

Key Concepts
This repository covers several important concepts in network programming and cybersecurity:

Sockets and Their Importance
Definition: Sockets are endpoints for sending and receiving data across a network.
Usage: They enable the creation of networked applications by providing a way to establish connections and transfer data.
Socket Module
Purpose: Part of the Python standard library, it provides low-level networking interfaces.
Key Functions:
socket(): Create a new socket.
bind(): Bind the socket to an address and port.
listen(): Enable the server to accept connections.
accept(): Accept a connection.
connect(): Connect to a remote socket.
send(): Send data.
recv(): Receive data.
close(): Close the socket.
Example Scripts
TCP Client Example
This script demonstrates a basic TCP client that connects to a specified IP address and port, receives data, and handles potential connection issues with exception handling and timeout settings.

python
```import socket

def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))

main()```

Port Scanner
This script performs a port scan on a target IP address to identify open ports, providing insights into available network services.

python
import socket

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))
portScanner(port)
TCP Server Example
This script sets up a TCP server that listens for incoming connections and sends a greeting message to connected clients.

python

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP
host = ''  # Listen on all available interfaces
port = 444  # Ensure the port is open and not blocked by firewalls

serversocket.bind((host, port))  # Bind the host and port to the socket object
serversocket.listen(3)  # Set up the TCP listener

print("Started Server")
print(f"Server Listening on {host}: {port}")

try:
    while True:
        clientsocket, address = serversocket.accept()
        try:
            print("Received connection from %s " % str(address))
            message = 'Hello! Thank you for connecting to the server' + "\r\n"
            clientsocket.send(message.encode('ascii'))
        finally:
            clientsocket.close()
except KeyboardInterrupt:
    print("\nServer has been interrupted. Server Socket Closing...")
    serversocket.close()

Setup and Installation
To set up the environment and run these scripts, follow these steps:

Install Python: Ensure Python 3.x is installed on your system.
Install Dependencies: Install the required Python modules.
pip install python-nmap

Setting Up Kali Linux with Docker (Optional)
If you prefer to run these scripts in a Kali Linux environment, you can use Docker to set up a containerized instance:

Pull the Kali Linux Docker Image:
docker pull kalilinux/kali-rolling

Run the Kali Linux Container:
docker run -t -i kalilinux/kali-rolling /bin/bash

Install Python in the Container:
apt update
apt install python3

Usage
Running the TCP Client
To run the TCP client script:
python3 tcp_client.py

Running the Port Scanner
To run the port scanner script:
python3 port_scanner.py

Running the TCP Server
To run the TCP server script:
python3 tcp_server.py
