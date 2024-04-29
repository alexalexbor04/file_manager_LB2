import os

def del_files(files):
    for name in files:
        if os.path.isfile(name):
            os.remove(name)
            print("\033[32m{}" .format(f'Файл {name} успешно удален'))
        else:
            print("\033[31m{}" .format(f'Файла {name} не существует'))