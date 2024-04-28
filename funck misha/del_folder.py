import os

def del_folder(name):
    try:
        os.rmdir(name)
        print(f'Папка удалена')
    except FileNotFoundError:
        print(f'Папка не существует')
    except OSError:
        print(f'Не удалось удалить папку так как в ней ест файлы, удалите сначала их')