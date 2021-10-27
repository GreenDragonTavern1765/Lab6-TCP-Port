import socket

def serverProgram(port):
    host = socket.gethostname()
    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(2)
    print('Waiting for clients to connect...')
    connection, address = serverSocket.accept()
    print('Connection Established: ' + str(address))

    connection.close()

if __name__ == '__main__':
    serverProgram(8000)