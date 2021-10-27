import socket
import datetime

def deviceInfo(host):
    print(host + '(' + socket.gethostbyname(host) +
          ') initialized @ ' + str(datetime.datetime.now()))

def clientProgram(port):
    host = socket.gethostname()
    deviceInfo(host)

    host = '192.168.1.153'
    clientSocket = socket.socket()
    print('Connecting to server...')
    try:
        clientSocket.connect((host, port))
    except(ConnectionRefusedError):
        print('--> ERROR: Connection denied')
        return
    print('Connection Established...')
    while True:
        now = datetime.datetime.now()
        time = '(' + now.strftime('%H:%M') + ')'
        print(time, end = ': ')
        message = input()
        clientSocket.send(message.encode())
    clientSocket.close()

if __name__ == '__main__':
    clientProgram(8000)
