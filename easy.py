import os


def get_path ():
    path = os.getcwd()
    return path

def show_dir ():
    print('Содержимое исходного каталога: {} '.format(os.listdir(get_path())))

def go (name):
    path = get_path()
    full_path_to_go = os.path.join(path, name)
    os.chdir(full_path_to_go)
    return full_path_to_go


def show (name):
    print('Содержимое текущего каталога: {} '.format(os.listdir(get_path())))


def rem_dir (name):
    path = get_path()
    full_path_to_go = os.path.join(path, name)
    os.rmdir(full_path_to_go)
    if not os.path.exists(name):
        print('Каталог {} успешно удален'.format(name))
    return full_path_to_go

def mk_dir (name):
    path = get_path()
    if os.path.exists(name):
        print('Нет. Каталог {} уже существует'.format(name))
    else:
        full_path_to_go = os.path.join(path, name)
        os.mkdir(full_path_to_go)
        if os.path.exists(name):
            print('Каталог {} успешно создан'.format(name))


