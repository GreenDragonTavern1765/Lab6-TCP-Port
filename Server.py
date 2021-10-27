import socket

def serverProgram():

    host = socket.gethostname()
    port = 8000

    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(2)
    connection, address = serverSocket.accept()
    print('Connection Established: ' + str(address))

    while True:
        clientData = connection.recv(1024).decode()
        if not clientData:
            break
        serverData = readFromFile(clientData)
        if serverData is None:
            connection.send('--> ERROR: File not found'.encode())
        else:
            connection.send(serverData.encode())

    print(type(connection))
    print('File contents successfully transfered...')
    print('Connection Terminated: ' + str(address))
    connection.close()

def readFromFile(fileName):
    try:
        file = open(fileName, "r")
    except FileNotFoundError:
        return None
    content = file.read()
    file.close()
    return content

if __name__ == '__main__':
    serverProgram()
