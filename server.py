# We are importing the socket module
import socket

# This is the server socket object where we specify the socket family and type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 and TCP

# We get the hostname and store it in the host variable
host = ''  # It can listen to all available interfaces if we use an empty string (Use if using an external environment or a docker container)
port = 444  # If you want to run this on Windows, make sure you run it as admin; on Kali, it may be different

serversocket.bind((host, port))  # Now we need to bind the host and port to the socket object

# We need to set up a TCP listener
serversocket.listen(3)  # We can specify how many connections we can listen to at a time

# Statement which would denote the server starting
print("Started Server")
# Port listening statement information 
print(f"Server Listening on {host}: {port}")
try:
    # Once the connection information is received, then
    while True:
        # We allow for the TCP information coming from the client to be accepted
        clientsocket, address = serversocket.accept()
        try:
            # Confirmation message for connection established
            print("Received connection from %s " % str(address))
            message = 'Hello! Thank you for connecting to the server' + "\r\n"
            # We would send the message via the send function
            clientsocket.send(message.encode('ascii'))
        finally:
            # We would terminate the connection
            clientsocket.close()
# Ctrl + C 
except KeyboardInterrupt:
    # Interruption message
    print("\nServer has been interrupted. Server Socket Closing...")
    # Action would close the server
    serversocket.close()