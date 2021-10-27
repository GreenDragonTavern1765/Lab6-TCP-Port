import socket
import datetime

def deviceInfo(host):
    print(host + '(' + socket.gethostbyname(host) +
          ') initialized @ ' + str(datetime.datetime.now()))

def serverProgram(port):
    host = socket.gethostname()
    deviceInfo(host)

    serverSocket = socket.socket()
    serverSocket.bind((host, port))

    serverSocket.listen(10)
    print('Searching for connections...')
    connection, address = serverSocket.accept()
    print('Connection Established: (' + str(address[0]) + ')')

    while True:
        clientData = connection.recv(1024).decode()
        if not clientData:
            break
        print(clientData)
    print('Connection Terminated: ' + str(address[0]))
    connection.close()

if __name__ == '__main__':
    serverProgram(8000)
