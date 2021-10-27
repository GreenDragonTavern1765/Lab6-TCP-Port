import socket

def serverProgram(port):
    host = socket.gethostname()
    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    while True:
        serverSocket.listen(10)
        print('Waiting for clients...')
        connection, address = serverSocket.accept()
        print('Connection established: Client = ' + str(address[0]))

        connection.close()

if __name__ == '__main__':
    serverProgram(8000)