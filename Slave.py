import time
import socket
import sys
import os

s = socket.socket()
host = '192.168.1.194'
port = 8000
s.connect((host, port))
print('connected to server')

command = s.recv(1024)
command = command.decode()

if command == 'open':
    print('command is: ', command)
    s.send('command received'.encode())

    os.system('ls')