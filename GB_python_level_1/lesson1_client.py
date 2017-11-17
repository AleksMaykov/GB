import socket
import sys


class Chat:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect(self):
       self.sock = socket.socket()
       self.sock.connect((self.host, self.port))

    def send(self, messege):
        self.sock.sendall(bytes(messege, 'utf-8'))

        print (self.sock.recv(2048).decode())



if __name__ == '__main__':

    chat = Chat('localhost', 7778)

    messeg = input('Привет!, пообщаемся? y\\n: ')

    if messeg == 'y':
        chat.connect()
        while True:
            data = chat.send (messeg)


    else:
        sys.exit()



