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
        print(str(addr), ":", receiveData.decode('utf-8'))



port = 8080

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', port))
serverSocket.listen(1)

print('--- %d번 포트로 접속 대기중입니다 ---' %port)

connectionSocket, addr = serverSocket.accept()

print('--- ', str(addr), '에서 접속하였습니다 ---')


sender = Thread(target=send, args=(connectionSocket,))
receiver = Thread(target=receive, args=(connectionSocket,))


sender.start()
receiver.start()

while True :
    time.sleep(1)
    pass