import socket
import requests

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

    print('File contents successfully transfered...')
    print('Connection Terminated: ' + str(address))
    writeToLogFile('logFile.txt')
    connection.close()

def writeToLogFile(logFile):
    file = open(logFile, "w")
    headers = {'content-type': 'multipart/form-data'}
    r = requests.post('http://localhost:63342/Lab6-TCP-Port/final.html?_ijt=j9mooak0t05ugronons8dupeec&_ij_reload=RELOAD_ON_SAVE', headers=headers)
    for i, j in r.headers.items():
        file.write(i + ":" + j + '\n')
    file.close()

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
