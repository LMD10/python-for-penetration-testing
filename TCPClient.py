# We import the socket module
import socket
#We follow the socket function and determine the family socket and the socket type
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#We would get the hosts name 
host = socket.gethostname()
#We would get the port 
port = 444
#We would connect both of these elements to the clientsocket
clientsocket.connect((host, port))
#We would have the message be the one that was sent in the server and determine the buffer size 
message = clientsocket.recv(1024)

#We close the connection to the clientsocket
clientsocket.close()
#We would decode the message that was received and specify the type  
print(message.decode('ascii'))