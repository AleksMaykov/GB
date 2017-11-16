# import os
# PATH = r"D:\GIT\python\setting"
# FILE_NAME = 'damages.txt'
#
# full_path = os.path.join(PATH, FILE_NAME)
#
#
# with open(full_path, 'r', encoding='UTF-8') as file:
#         for el in file:
#             print(el)


# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# def about_user (name, age, city):

# Функция принимает имя, возраст и город пользователя и возвращает форматированную строку с этими данными

#     result = '{}, {} год(а), проживанет в городе {}'.format(name, age, city)
#     return result
#
# name = input('Привет! Укакжите свое имя, пожалуйста: ')
# age = input('Укажите Ваш возраст: ')
# city = input('Укажите город Вашего проживания: ')
#
# result = about_user(name, age, city)
# print(result)

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# def max_number(a, b, c):

## Функция принимает 3 числа и возвращает самое большое из них

#     num_list = [a,b,c]
#     max_num = (max(num_list))
#     return max_num
#
# num_1 = int (input('Введите значение первого числа: '))
# num_2 = int (input('Введите значение второго числа: '))
# num_3 = int (input('Введите значение третьего числа: '))
#
# result = max_number(num_1, num_2, num_3)
# print('Максимальное число из введеных вами: {}'.format(result))


# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов

# def max_str (* arg):
#
# # Функция принмает произвольное число строк, сравнивает их и возвращает самую длянную из них
#
#     max_len = max (arg, key = len)
#     return max_len
#
#
# arg_1 = input('Введите первыю строку: ')
# arg_2 = input('Введите вторую строку: ')
# arg_3 = input('Введите трутью строку: ')
#
# result = max_str(arg_1, arg_2, arg_3)
# print('Самая дилинная строка это: : {}'.format(result))

################################################################################################

# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь name - строка полученная от пользователя,
# health - 100, damage - 50.
# Теперь надо создать функцию attack(person, person) функция в качестве аргумента будет
# принимать атакующего и атакуемого, функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого

# import random
# import time
# import math
#
#
# def player ( **kwargs):
#     person = 'Великий {} {} мы приветствуем тебя на нашей битве! Помни, что твой уровень здоровья равен {}%,  сила удара {}'.format(kwargs['type_of_warrior'], kwargs['name'], kwargs['health'], kwargs['damage'])
#     return person
#
# def attack (health, damage):
#     if health > 0:
#         armor = random.randrange(0, 2)
#         arg_armor = random.randrange (1 , 7)
#         if armor ==1:
#             health = health - (damage*(arg_armor/10))
#             protection = 'Броня смягчила удар.'
#         else:
#             health -= damage
#             protection = 'Удар сквозь броню.'
#
#     else:
#         health <= 0
#
#     return (math.trunc(health),protection)
#
#
#
# type_list = {'1': 'Воин', '2':'Эльф', '3':'Орк'}
# names_of_enemy = {'1': '\'Могучий Слон\'', '2':'\'Меткий Глаз\'', '3':'\'Несокрушимая Стена\''}
# damage_man = random.randrange(10,30)
# damage_elf = random.randrange(5, 40)
# damage_ork = random.randrange(0,50)
# health_full = 100
# health = health_full *2
# health_enemy = health_full
#
# type_of_warrior = input('Выберите кем Вы будете 1 - Воин, 2 - Эльф, 3 - Орк: ')
# name = input('Введите свое имя: ')
#
# if type_of_warrior == '1':
#     damage = damage_man
#     playman = {'type_of_warrior': 'Воин', 'name': name.title(), 'health': health_full, 'damage': damage}
# elif type_of_warrior == '2':
#     damage = damage_elf
#     playman = {'type_of_warrior': 'Эльф', 'name': name.title(), 'health': health_full, 'damage': damage}
# elif type_of_warrior == '3':
#     damage = damage_ork
#     playman = {'type_of_warrior': 'Орк', 'name': name.title(), 'health': health_full, 'damage': damage}
# else:
#     print('ЭЭЭЭ СТОП! Вы неверно выбрали расу. До свидания.')
#     time.sleep(3)
#     exit()
#
#
#
# time.sleep(2)
#
# enemy  = str (random.randrange(1,4))
#
# if enemy == '1':
#     damage_enemy = damage_man
# elif enemy == '2':
#     damage_enemy = damage_elf
# elif enemy == '3':
#     damage_enemy = damage_ork
#
#
# print('Ваш соперник {} {}.'.format(type_list[enemy], names_of_enemy[enemy]))
# time.sleep(3)
#
# print(player(**playman))
#
# time.sleep(2)
# while health > 0:
#     if health_enemy > 0:
#         kick = input('Нанести удар? y/n: ')
#         if kick == 'y':
#             health_enemy, protection = attack(health_enemy, damage)
#             print('Вы нанесли урон, уровень здоровья вашего противника равен: {}%. {}'.format(health_enemy, protection))
#             time.sleep(3)
#             health, protection = attack(health, damage_enemy)
#             print('Вам нанесли урон, ваш уровень здоровья равен: {}%. {}'.format(health, protection))
#         else:
#             print('Слабак, сбежал с поля боя')
#             time.sleep(3)
#             exit()
#     else:
#         print('ТАДА!!!! ПОБЕДА!! {} {} вы победили в честной схватке! У Вас осталое еще {}HP.'.format(type_list[enemy], names_of_enemy[enemy],health))
#         any = input('Пресс эни кей')
#         exit()
#
# else:
#     print('THE END. {} {} вы пали геройской смертью'.format(type_list[type_of_warrior], name))
#
# any = input('Пресс эни кей')
# exit()

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 0.7
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, каждую в свой файл, в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

import random
import time
import math


def player ( **kwargs):
    person = 'Великий {} {} мы приветствуем тебя на нашей битве! Помни, что твой уровень здоровья равен {}%,  сила удара {}'.format(kwargs['type_of_warrior'], kwargs['name'], kwargs['health'], kwargs['damage'])
    return person

def attack (health, damage):
    if health > 0:
        armor = random.randrange(0, 2)
        arg_armor = random.randrange (1 , 7)
        if armor ==1:
            health = health - (damage*(arg_armor/10))
            protection = 'Броня смягчила удар.'
        else:
            health -= damage
            protection = 'Удар сквозь броню.'

    else:
        health <= 0

    return (math.trunc(health),protection)



type_list = {'1': 'Воин', '2':'Эльф', '3':'Орк'}
names_of_enemy = {'1': '\'Могучий Слон\'', '2':'\'Меткий Глаз\'', '3':'\'Несокрушимая Стена\''}
damage_man = random.randrange(10,30)
damage_elf = random.randrange(5, 40)
damage_ork = random.randrange(0,50)
health_full = 100
health = health_full *2
health_enemy = health_full

type_of_warrior = input('Выберите кем Вы будете 1 - Воин, 2 - Эльф, 3 - Орк: ')
name = input('Введите свое имя: ')

if type_of_warrior == '1':
    damage = damage_man
    playman = {'type_of_warrior': 'Воин', 'name': name.title(), 'health': health_full, 'damage': damage}
elif type_of_warrior == '2':
    damage = damage_elf
    playman = {'type_of_warrior': 'Эльф', 'name': name.title(), 'health': health_full, 'damage': damage}
elif type_of_warrior == '3':
    damage = damage_ork
    playman = {'type_of_warrior': 'Орк', 'name': name.title(), 'health': health_full, 'damage': damage}
else:
    print('ЭЭЭЭ СТОП! Вы неверно выбрали расу. До свидания.')
    time.sleep(3)
    exit()



time.sleep(2)

enemy  = str (random.randrange(1,4))

if enemy == '1':
    damage_enemy = damage_man
elif enemy == '2':
    damage_enemy = damage_elf
elif enemy == '3':
    damage_enemy = damage_ork


print('Ваш соперник {} {}.'.format(type_list[enemy], names_of_enemy[enemy]))
time.sleep(3)

print(player(**playman))

time.sleep(2)
while health > 0:
    if health_enemy > 0:
        kick = input('Нанести удар? y/n: ')
        if kick == 'y':
            health_enemy, protection = attack(health_enemy, damage)
            print('Вы нанесли урон, уровень здоровья вашего противника равен: {}%. {}'.format(health_enemy, protection))
            time.sleep(3)
            health, protection = attack(health, damage_enemy)
            print('Вам нанесли урон, ваш уровень здоровья равен: {}%. {}'.format(health, protection))
        else:
            print('Слабак, сбежал с поля боя')
            time.sleep(3)
            exit()
    else:
        print('ТАДА!!!! ПОБЕДА!! {} {} вы победили в честной схватке! У Вас осталое еще {}HP.'.format(type_list[enemy], names_of_enemy[enemy],health))
        any = input('Пресс эни кей')
        exit()

else:
    print('THE END. {} {} вы пали геройской смертью'.format(type_list[type_of_warrior], name))

any = input('Пресс эни кей')
exit()


############################################################################################

# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Есть условие, не отображать людей получающих более зарплату 500000
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату - 13% (налоги ведь),
# где имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.
names = ['Vasya', 'Anton', 'Oleg', 'Sergey', 'Alexandr', 'Andrey']
salary = [10000, 15000, 710000, 18000, 13500, 1000000]