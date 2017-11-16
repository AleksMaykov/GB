import sys
import turtle
import random
import time


max_number = int (turtle.numinput('Введите максимальное число для игпы', 'число ', 1, 1, 10000000))

max_num_str = str (max_number)

a=random.randint(1, max_number)
print(a)

def gotoxy(x,y):
    turtle.color('black')
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    turtle.color('black')
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

def say_yes ():
    gotoxy(-150, 200)
    turtle.color('white')
    turtle.write('Неверно!',
                 font=('Arial', 28, 'bold'))
    turtle.color('green')
    turtle.write('Ура! Победа!',
                 font=('Arial', 28, 'bold'))
def say_no():
    gotoxy(-150, 200)
    turtle.color('white')
    turtle.write('Ура! Победа!',
                 font=('Arial', 28, 'bold'))
    turtle.color('red')
    turtle.write('Неверно!',
                 font=('Arial', 28, 'bold'))

def say_out():
    gotoxy(-150, 250)
    turtle.color('white')
    turtle.write('Неверно!',
                 font=('Arial', 28, 'bold'))
    turtle.color('red')
    turtle.write('Вы проиграли!',
                 font=('Arial', 48, 'bold'))

def say_help(more_or_less):
    gotoxy(-200, 150)
    turtle.color('blue')
    turtle.write('Почти, почти....попробуй выбрать число ' + more_or_less,
                 font=('Arial', 12, 'bold'))
    time.sleep(3)
    turtle.color('white')
    turtle.write('Почти, почти....попробуй выбрать число ' + more_or_less,
                 font=('Arial', 12, 'bold'))

coord_list = []
coord = open('docs\cordinate.txt')

for line in coord:
    line  = line.strip().split(',')
    nums = []
    for n in line:
         nums.append(int(n))
    coord_list.append(nums)



answer = turtle.textinput('Играть?', "y/n")

if answer == 'n':
    sys.exit()
if answer == 'y':
    pass
else:
    sys.exit()

try_count = 0

while True:
    number = turtle.numinput('Угадайте число', 'число от 1 до ' + max_num_str, 1, 1, max_number)
    if number == a:
         say_yes()
         time.sleep(5)
         break

    else:
        say_no()
        if try_count != 4:
            draw_line(*coord_list[try_count])
        else:
            gotoxy(-100,-10)
            turtle.circle (25)
        try_count += 1

        if number > a:
            say_help('поменьше')
        else:
            say_help('побольше')

        if try_count == 10:
            say_out()
            time.sleep (3)
            sys.exit()




