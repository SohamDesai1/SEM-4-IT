import socket
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
 
# recv message and decode here 1024 is buffer size.   
print (s.recv(1024).decode())  
s.close()
