from socket import *
from threading import Thread
import time

def send(sock) :
    while True :
        sendData = input('')
        sock.send(sendData.encode('utf-8'))

def receive(sock) :
    while True :
        receiveData = sock.recv(1024)
        print("server :", receiveData.decode('utf-8'))


port = 8080

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', port))

print('--- 접속이 완료되었습니다 ---')

sender = Thread(target=send, args=(clientSocket,))
receiver = Thread(target=receive, args=(clientSocket,))

sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass
