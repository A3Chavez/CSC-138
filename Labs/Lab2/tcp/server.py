from socket import *
from time import sleep
serverPort = 12003
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("Starting up server", end = " ", flush = True)
sleep(.5)
print (".", end = " ", flush = True)
sleep(.5)
print (".", end = " ", flush = True)
sleep(.5)
print (".", end = " ", flush = True)
sleep(.5)
print (". The server is ready to receive!")
while 1:
	connectionSocket, addr = serverSocket.accept()

	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()