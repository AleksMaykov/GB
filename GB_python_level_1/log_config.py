import datetime
import os

FILE_NAME = 'log.txt'
# PATH = os.getcwd()
# file_path_full = os.path.join(PATH, FILE_NAME)


def log (func):

    def wraper(*args, **kwargs):

        result = func(*args, **kwargs)

        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'a+') as f:
                f.write('\ntime:{} name:{} ({}, {}) = {}'.format(datetime.datetime.now(), func.__name__, args, kwargs, result))
        else:
            with open(FILE_NAME, 'w') as f:
                f.write('\ntime:{} name:{} ({}, {}) = {}'.format(datetime.datetime.now(), func.__name__, args, kwargs, result))

        return result
    return wraper



# @log
# def add(a,b):
#     return  a + b
#
#
# c = add(3, 7)
# print(c)
# with open('log.txt', 'r+') as f:
#     f.write('0123456789')
