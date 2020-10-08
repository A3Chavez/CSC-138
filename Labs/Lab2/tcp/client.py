from socket import *
serverName = '10.0.0.236'
serverPort = 12003
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Please type a lowercase sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode("utf-8")
print ("From Server: ", modifiedSentence)
clientSocket.close()