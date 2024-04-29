import os

def del_folder(name):
    try:
        os.rmdir(name)
        print("\033[32m{}" .format('Папка удалена'))
    except FileNotFoundError:
        print("\033[31m{}" .format('Указанная папка не найдена'))
    except OSError:
        print("\033[31m{}" .format('Не удалось удалить папку так как в ней ест файлы, удалите сначала их'))