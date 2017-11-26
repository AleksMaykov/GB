import sys
import socket
import select
import logging
from log_config import log


logging.basicConfig(
    filename="test.log",
    level=logging.DEBUG,
    filemode  = 'w',
    format="%(asctime)s : %(levelname)s : %(module)s : %(funcName)s : %(message)s")

logg = logging.getLogger('Server')

class Server(object):

    def __init__(self, host, port):

        self._host = host
        self._port = port
        self._sock = socket.socket()
        self._sock.bind((str(self._host), int (self._port)))
        logg.info("Server create to {} at port {}".format(self._host, self._port))
        self._clients = list()

    # @property
    # def tcp_socket(self):
    #     return self._sock

    @log
    def _get_message(self, client, responces):

        data = client.recv(1024).decode('utf-8')
        responces[client] = data
        logg.info("Get message: {} from {}".format(data, client))

    @log
    def _send_message(self, client, responces):

        responce = responces[client].encode('utf-8')
        client.send(responce.upper())
        logg.info("Send message: {} to {}".format(responces[client], client))

    def _read(self, r_clients):

        responces = dict()

        for client in r_clients:

            try:

                self._get_message(client, responces)

            except Exception as err:

                print(err)
                logg.error('client {} {} disconnected.'.format(client.fileno(), client.getpeername()))
                self._clients.remove(client)

        return responces

    def _write(self, responces, w_clients):

        for client in w_clients:

            if client in responces:

                try:

                    self._send_message(client, responces)

                except:

                    logg.error('client {} {} disconnected.'.format (client.fileno(), client.getpeername()))
                    self._clients.remove(client)
                    client.close()
                    self._clients.remove(client)

    @log
    def _add_client(self, client):
        self._clients.append(client)


    def run(self, how_many_clients):

        self._sock.listen(int(how_many_clients))
        self._sock.settimeout(0.2)

        while True:

            try:

                client, addr = self._sock.accept()


            except KeyboardInterrupt:

                logg.error('Server disabled')
                self._sock.close()
                sys.exit()

            except OSError as err:
                pass

            else:

                logg.info('Подключился пользователь {}'.format(addr))
                self._add_client(client)

            finally:

                r_clients = list()
                w_clients = list()

                try:

                    r_clients, w_clients, ex_clients = select.select(self._clients, self._clients, [], 0)

                except:

                    pass

                responces = self._read(r_clients)

                self._write(responces, w_clients)




if __name__ == '__main__':

    server = Server('localhost', 7777)
    server.run(5)


                except Exception as err:

                    print(err)
                    print('Client {} {} disconnect'.format(client.fileno(), client.getpeername()))

                    client.close()
                    self._clients.remove(client)


    def run(self, how_many_clients):

        self._sock.bind((str(self._host), int(self._port)))
        self._sock.listen(int (how_many_clients))
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
