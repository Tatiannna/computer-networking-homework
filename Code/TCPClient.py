#Tatianna Robinson

from socket import *

serverName = '127.0.0.1'
serverPort = 9999
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = raw_input("Enter a sentence: ")
clientSocket.send(sentence)

command = raw_input("Enter '1' to capitalize, '2' to set to lowercase and '3' to reverse: ")
clientSocket.send(command)

modifiedSentence = clientSocket.recv(1024)

print "From Server: ", modifiedSentence
clientSocket.close()
