#Tatianna Robinson

from socket import *

serverPort = 9999
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")
while 1:

	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	command = connectionSocket.recv(1024)

	if command == '1':
		connectionSocket.send(sentence.upper())
	elif command == '2':
		connectionSocket.send(sentence.lower())
	elif command == '3':
		connectionSocket.send(sentence[::-1])
	else:
		connectionSocket.send("No such commnand")

	connectionSocket.close()
