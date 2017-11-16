import os, sys, shutil
import psutil

def sys_info():
    print('Текущая директория равна: ' + os.getcwd())
    print('Количество ядер на CPU: ' + str(os.cpu_count()))
    print('Логин текущего пользователя: ' + os.getlogin())
    print('Версия платформы: ' + sys.platform)
    print('Кодировка файловой системы:  ' + sys.getfilesystemencoding())

def copy_file (file_list):
    copy_count = 0
    for file in file_list:
        if os.path.isfile(file):
            fullname = (file + '.dupl')
            shutil.copy(file, fullname)
            if os.path.exists(fullname):
                print('Новый файл ' + fullname + ' создан')
                copy_count += 1

            else:
                print('Упс. с копированием возникли проблемы')
    return (copy_count)


def del_file (file_list):
    del_count = 0
    for file in file_list:
        fullname = os.path.join(os.getcwd(), file)
        if fullname.endswith('.dupl'):
            os.remove(fullname)
            if not os.path.exists(fullname):
                del_count += 1
    return(del_count)
def main():
    print('Привет Олень!')
    print('Добро пожаловать, ну или типа того')

    name = input('Кстати, а как тебя зовут?: ')

    print('Хм... ' + name + '? оригинальненько, но ладно пусть так пока.')

    answer = ''

    while answer != 'q':
        answer = input('Работать будем? y/n/q: ')
        if answer == 'y':
            print('Это замечательно!')
            print('Я умею следующее:')
            print('Выведу список файлов в каталоге [1]:')
            print('Выведу информацию о системе [2]:')
            print('Выведу PID всех запущенных процессов [3]:')
            print('оздам файлы dupl в текущей директории [4]:')
            print('Удалю файлы dupl в текущей директории [5]:')
            # print('Удалю дублированные файлы в текущей директории [6]:')
            do = int (input('Укажите номер действия: '))
            if do == 1:
                 print(os.listdir())

            elif do == 2:
                sys_info()

            elif do == 3:
                 print(psutil.pids())

            elif do == 4:
                 file_list = os.listdir()
                 copy_count = copy_file(file_list)
                 print('Всего создано ' + str(copy_count) + ' файлов')

            elif do == 5:
                file_list = os.listdir()
                del_count = del_file(file_list)
                print('Всего удалено ' + str(del_count) + ' дубликатов')



            # elif do == 6:
            #     list1 = os.listdir()
            #     list2 = os.listdir()
            #     for file in list1:
            #         for file1 in list2:
            #             if file == file1:
            #                 os.remove(file1)




            else:
                pass

        elif answer =='n':
            print('.... тунеядец')
        elif answer == 'q':
            print('Пакапака.....')
        else:
            print('ну определтсь уже')

    # my_list = [3, 45, True, 'LALALA', 212.56, 3 , False, 'Oh NO!', 2.456]
    # print(my_list)
    # sort_list = []
    # for num in my_list:
    #     if type (num) == int:
    #         sort_list.append(num)


if __name__ == '__main__':
    main()