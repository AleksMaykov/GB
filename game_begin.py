# https://yadi.sk/d/bhwJI7M03JFmij - картинки к игре
# Подключение модулей
import os, sys, shutil

# Модуль tkinter - для создания GUI
from tkinter import *
from random import choice

# PEP 8
# Для работы с графикой воспользуемся дополнительной библиотекой - PIL
# Необходимо установить библиотеку Pillow:  pip install Pillow


SIDE = 4  # <- величина стороны квадрата (для пятнашек квадрат 4х4)


def key_press(btn):
    ''' Работа с кнопками
    '''
    print(btn)


# Создаём главное окно приложения
main_window = Tk()

# Задаём заголовок окна
main_window.title('Пятнашки')

label = Label(main_window, text='Hello')
label.pack()


# Нажатия стрелок на клавиатуре привызываем к главному окну:
main_window.bind('<Right>', lambda e: key_press('r'))
main_window.bind('<Left>', lambda e: key_press('l'))
main_window.bind('<Up>', lambda e: key_press('u'))
main_window.bind('<Down>', lambda e: key_press('d'))


# Запуск главного цикла обработки сообщений графической оболочки:
main_window.mainloop()
