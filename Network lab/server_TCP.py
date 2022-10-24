import socket

s = socket.socket()    
host = socket.gethostname() 
port = 12345
s.bind((host, port))

while True:
   c, addr = s.accept()       
   print ('Connection Established')
   a = 'Hello this is a TCP connection program'
   d = str(a)
   c.send(d.encode())     
c.close()
