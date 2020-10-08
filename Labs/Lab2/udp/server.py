from socket import *
from time import sleep
serverPort = 12003
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
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
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)