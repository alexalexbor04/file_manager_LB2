import os

def make_folder(name):
    try:
        os.mkdir(name)
        print(f'Папка создана')
    except:
        print(f'Не удалось создать папку. Она уже существует.')