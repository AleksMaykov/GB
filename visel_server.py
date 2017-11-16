
import random
import socketserver

HOST = 'Localhost'
PORT = 9999

class GibbetHendler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode()

        print('Клиент {} сообщает:  {}'.format(self.client_address[0], self.data))

        x = random.randint (1, 100)
        if self.data =='START':
            self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
            try_count = 10
            while True:
                self.data = self.request.recv(1024).decode()
                data = self.data.split(';')
                if data[0] =='TRY':
                    if int(data[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        break
                    else:
                        try_count -=1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            break
                        else:
                            self.request.sendall(bytes('FALSE', 'utf-8'))
                elif data[0] =='GOODBYE':
                    print('Клиент слился... слабак.')

server = socketserver.TCPServer((HOST, PORT), GibbetHendler)
print('Сервер запущен')

server.serve_forever()