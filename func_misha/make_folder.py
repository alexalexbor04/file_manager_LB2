import os

def make_folder(name):
    try:
        os.mkdir(name)
        print("\033[32m{}" .format(f'Папка создана'))
    except:
        print("\033[31m{}" .format(f'Не удалось создать папку. Она уже существует.'))