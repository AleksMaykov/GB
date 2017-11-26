import socket

class Client(object):

    def __init__(self, host, port):

        self._host = str(host)

        self._port = int(port)

    def run(self):

        with socket.socket() as sock:

            self.socket = sock

            self.socket.connect((self._host, self._port))
            print('Приветсвую путник! Запомни exit это выход)')

            while True:

                msg = input('Введите сообщение: ')

                if msg == 'exit':

                    break

                sock.send(msg.encode('utf-8'))

                data = sock.recv(1024).decode('utf-8')

                print('Поступил ответ: ', data)


if __name__ == '__main__':

    client = Client('localhost', 7777)

    client.run()
    # sock = socket.socket()

    # sock.connect(('localhost', 8005))


    # massage = sock.recv(1024)

    # sock.close()

    # print(massage)

