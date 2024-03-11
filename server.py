from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = input("Enter port number: ")

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\n'.encode())
        connectionSocket.send('Content-Type: text/html\n'.encode())
        connectionSocket.send('\n'.encode())
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        header = 'HTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(header.encode())
        connectionSocket.close()