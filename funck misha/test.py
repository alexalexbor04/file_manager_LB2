import os

def del_files(files):
    for name in files:
        if os.path.isfile(name):
            os.remove(name)
            print(f'Гатова')
        else:
            print(f'нету')