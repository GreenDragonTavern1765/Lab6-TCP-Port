import socket
from datetime import datetime

def clientProgram():

    host = socket.gethostname()
    port = 8000

    clientSocket = socket.socket()
    clientSocket.connect((host, port))
    print('Connection Established...')

    message = input(' -> ')
    clientSocket.send(message.encode())
    data = clientSocket.recv(1024).decode()

    while (data == '--> ERROR: File not found'):
        print('--> ERROR: File not found')
        message = input(' -> ')
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024).decode()
    makeHTML(data)

    print('File successfully transfered...')
    print('Connection Terminated... ')
    clientSocket.close()

def makeHTML(contents):

    list = contents.splitlines()
    for i in range(0, len(list)):
        if list[i] == '</body>':
            break

    now = datetime.now()
    ipAddress = "\t<p>My IP Address is " + str(socket.gethostbyname(socket.gethostname())) + "</p>"
    date = "\t<p>Date and Time is " + str(now) + "</p>"

    list.insert(i, date)
    list.insert(i, ipAddress)
    result = '\n'.join(list)
    writeHTML(result)

def writeHTML(contents):
    file = open("final.html", "w")
    file.write(contents)
    file.close()

if __name__ == '__main__':
    clientProgram()


