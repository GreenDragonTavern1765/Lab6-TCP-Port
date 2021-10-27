import socket
from datetime import datetime

# Write a program which specifies at run time:
#   • a port number on which to listen for incoming connections.
#   • the name of a log file

def clientProgram(port):
    host = '192.168.1.153'

    clientSocket = socket.socket()
    print('Attempting to connect...')
    try:
        clientSocket.connect((host, port))
    except(ConnectionRefusedError):
        print('--> ERROR: Connection denied')
    else:
        print('Connection Established...')
    clientSocket.close()

if __name__ == '__main__':
    clientProgram(8000)