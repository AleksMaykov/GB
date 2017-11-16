
import socket

HOST = 'Localhost'
PORT = 9999

print('Клиент игры "ВиселицО" приветствует вас')
print('Подключение к серверу ...... {}:{}'.format(HOST,PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

sock.sendall(bytes('START', 'utf-8'))

data = sock.recv(1024).decode()
data = data.split(';')

if data[0] =='GUESS':
    print ('Угадайте число от {} до {}. У Вас 10 попыток'.format(data[1],data[2]))
    while True:
        x = input('Ваш ответ: ')
        if x == 'q':
           break

        sock.sendall(bytes('TRY'.format(x), 'utf-8'))
        data = sock.recv(1024).decode()
        data = data.split(';')

        if data[0] == 'TRUE':
            print('Вы угадали!')
            break
        elif data[0] == 'FALSE':
            print('Вы неправы. Еще есть попытки...')
        elif data[0] == 'FAIL':
            print('Вы неугадали')
            break

sock.sendall(bytes('GOODBYE', 'utf-8'))
sock.close()