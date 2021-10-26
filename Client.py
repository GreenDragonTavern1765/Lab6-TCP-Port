import socket
from datetime import datetime

# Write a program which specifies at run time:
#   • a port number on which to listen for incoming connections.
#   • the name of a log file

def clientProgram():
    host = socket.gethostname()
    print(host)

if __name__ == '__main__':
    clientProgram()