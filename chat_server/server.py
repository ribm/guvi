import socket
import sys
import time
s =socket.socket()
host = socket.gethostname()
print("server will start the host:", host)
port = 4444

s.bind((host,port))
print("succesfully")

s.listen(1)
conn, addr = s.accept()
print("addr has conneted", addr)


while 1:
    
    message = input(str("you==>"))
    message = message.encode()
    conn.send(message)
    incoming_message =conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("client==>", incoming_message)