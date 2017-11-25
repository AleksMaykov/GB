import socket
# import json
import sys


class Chat(object):
    def __init__(self, host, port):
        self.host = str (host)
        self.port = int(port)



    # def make_messege(self, text):
    #
    #     self.message_text = text
    #     self.message_object = {'message': self.message_text, 'from': 'User1'}
    #     self.message_string = json.dumps(self.message_object)
    #     self.message_bytes = self.message_string.encode('utf-8')
    #     return (self.message_bytes)


    # def send_and_print(self, messege):
    #
    #     self.sock.sendall(messege)
    #     print (self.sock.recv(2048).decode())

    def run(self):
        with socket.socket() as sock:
            self.socket = sock
            self.socket.connect((self.host, self.port))

            while True:
                meassege = input('Введите сообщение: ')

                if meassege == 'exit':
                    self.socket.close()
                    sys.exit()


                sock.send(meassege.encode('utf-8'))
                data = sock.recv(1024).decode('utf-8')
                print(data)


if __name__ == '__main__':

    chat = Chat('localhost', 7777)
    chat.run()

