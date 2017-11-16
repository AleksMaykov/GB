import random
import time
import math

class Warrior:

    def __init__(self, type, name):
        self.type = type
        self.name = name

    def start_value(self):
        self.type_list = {'1': 'Воин', '2': 'Эльф', '3': 'Орк'}
        self.names_of_enemy = {'1': '\'Могучий Слон\'', '2': '\'Меткий Глаз\'', '3': '\'Несокрушимая Стена\''}
        self.damage_man = random.randrange(10, 30)
        self.damage_elf = random.randrange(5, 40)
        self.damage_ork = random.randrange(0, 50)
        self.health_full = 100
        self. health = self.health_full * 2
        self. health_enemy = self.health_full

    def create_warrior(self):
        pass



class Man(Warrior):

    def __init__(self):
        super (Warrior, self).__init__()


class Enemy (Warrior):

    def __init__(self):
        super(Warrior, self).__init__()



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