from socket import *
serverName = '10.0.0.236'
serverPort = 12003
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Please type a lowercase sentence: ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())
clientSocket.close()