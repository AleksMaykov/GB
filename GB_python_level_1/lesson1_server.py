import socket
import sys
import select


class ServerChat(object):

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock  = socket.socket()
        self._sock.bind((str(self._host), self._port))
        self._clients = list()

    # def decode(self, message_bytes):
    #     self.message_string = message_bytes.decode('utf-8')
    #     self.message_object = json.loads(self.message_string)
    #     self.from_user = self.message_object.get('from')
    #     self.message_text = self.message_object.get('message')

    def _read(self, r_clients):

        responces = dict()

        for client in r_clients:

            try:
                data = client.recv(1024).decode('utf-8')
                responces[client] = data


            except Exception as err:

                print(err)
                print('Client {} {} disconnect'.format(client.fileno(), client.getpeername()))
                self._clients.remove(client)

        return responces


    def _write(self, responces , w_clients):

        for client in w_clients:

            if client in responces:

                try:
                    responces = responces[client].encode('utf-8')
                    client.send(responces)


                except Exception as err:

                    print(err)
                    print('Client {} {} disconnect'.format(client.fileno(), client.getpeername()))

                    client.close()
                    self._clients.remove(client)


    def run(self, how_many_clients):

        self._sock.listen(how_many_clients)
        # self._sock.settimeout(0.2)

        print('Сервер запущен')

        while True:

            try:
                client, addr = self._sock.accept()
                print('*' * 50 + '\nПодключился пользователь {}\n'.format(addr) + '*' * 50)

            except Exception as err:
                 print('Сервер выключен. Причина: {}'.format(err))
                 self._sock.close()
                 sys.exit()

            else:
                self._clients.append(client)
                r_clients, w_clients, err_clients = select.select(self._clients, self._clients, [])
                responces = self._read(r_clients)
                self._write(responces, w_clients)
                print(r_clients)
                print(w_clients)

if __name__ == '__main__':

    chat = ServerChat('localhost', 7777)
    chat.run(5)
