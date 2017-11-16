# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys
import re
import shutil
import easy

# choise = input('Выбурите, что вы хотите: 1 - создать 9 папок, 2 - удалить 9 папок? ')
#
# PATH = os.getcwd()
# DIR_NAME = 'dir_'
#
# path_full = os.path.join(PATH,DIR_NAME)
#
# if choise == '1':
#     try:
#         for i in range (10):
#             full_dir_name = path_full + str (i)
#             os.mkdir(full_dir_name)
#         print('Папки от dir_1 до dir_9 созданы успешно')
#     except FileExistsError:
#         print('Вы что то перепутали и данные папки уже существуют')
#
# elif choise == '2':
#     try:
#         for i in range (10):
#             full_dir_name = path_full + str (i)
#             os.rmdir(full_dir_name)
#         print('Папки от dir_1 до dir_9 удалены успешно')
#     except FileNotFoundError:
#         print('''
#         Упс!
#         Что бы продать что-нибудь ненужное, нужно сначала купить что-нибудь не нужное.
#         Создайте для начала папки.
#         ''')
# else:
#     print('Вы сделали неверный выбор')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#
# dir = os.listdir(path=".")
# print(dir)
# for i in dir[:]:
#     if re.findall('[a-z_A-Z]+\.[a-z]+',i)== None:
#         print(i)
#         dir.remove(i)
# print('#' * 20)
# print(dir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# PATH = os.getcwd()
# file_name = os.path.basename(__file__)
#
#
# if os.path.isfile(file_name):
#     fullname = (file_name + '.copy')
#     shutil.copy(file_name, fullname)
#     if os.path.exists(fullname):
#         print('Новый файл ' + fullname + ' создан')
#     else:
#         print('Упс. с копированием возникли проблемы')

###################################################################################

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

#


#
#
# print('Добро пожаловать в Утилиту Вер.1')
# choise = input('Работаем? y\\n: ')
#
# while choise == 'y':
#     user_choise = input('''
#     Выберите действие которе необходимо выполнить:
#     # 1. Перейти в папку
#     # 2. Просмотреть содержимое текущей папки
#     # 3. Удалить папку
#     # 4. Создать папку
#     Утилита ожидает ввода Вашего выбора: ''')
#
#
#     if user_choise == '1':
#         easy.show_dir()
#         go_path = input('Введите адрес каталога для перехода: ')
#         path_name = easy.go(go_path)
#         print('Вы перешли в каталог: {} '.format(path_name))
#
#     elif user_choise == '2':
#         path = easy.get_path()
#         easy.show(path)
#
#     elif user_choise == '3':
#         easy.show_dir()
#         go_path = input('Введите имя каталога для удаления: ')
#         path_name = easy.rem_dir(go_path)
#         print('Вы успешно удалили каталог: {} '.format(path_name))
#
#     elif user_choise == '4':
#         easy.show_dir()
#         go_path = input('Введите имя создаваемого каталога: ')
#         path_name = easy.mk_dir(go_path)
#
#
#     else:
#         print('Вы ввели неверный набор символов')
#         break




########################################################################################################
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")