import socket
import sys
import datetime
PORT = 7778

if __name__ == '__main__':

    sock = socket.socket()
    sock.bind(('localhost', PORT))
    sock.listen(5)
    print('Сервер запущен')

    while True:

        try:
            client, addr = sock.accept()
            print('Подключился пользователь с адресом и портом {}'.format(addr))
            data = client.recv(2048).decode()

            if data == 'y':
                client.send(bytes ('Здравствуйте, мы ради привествовать нас в нашей программе','utf-8'))
                name = client.send(bytes('Представьтесь, пожалуйста. Ваше имя?: ', 'utf-8'))
                email = client.send(bytes('Укажите Ваш email адрес: ', 'utf-8'))






            else:
                print('Сервер выключен. До свидания')
                sys.exit()

            # time = datetime.datetime.now()
            # time_str = time.strftime('%d - %B - %Y')
            # client.send(time_str.encode('utf-8'))




        except Exception as err:
            print('Сервер выключен. Причина: {}'.format(err))
            sys.exit()


