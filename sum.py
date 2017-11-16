import os
import sys

def my_sum (* args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


print('sys_argv = ', sys.argv)

def print_help():
    print('help - получение справки')
    print('mkdir <dir_name> - создание каталога')
    print('ping - тестовый ключ')


def make_dir():
    if not dir_name:
