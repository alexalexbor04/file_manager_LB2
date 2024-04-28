import os
import shutil

def del_folder(name):
    try:
        os.rmdir(name)
        print(f'Yes')
    except FileNotFoundError:
        print(f'No')
    except OSError:
        print(f'asd')

def files_copying(first, sec, files):
    if not os.path.isdir(first) or not os.path.isdir(sec):
        print('папка(')
        return
    for i in files:
        if os.path.isfile(os.path.join(first, i)):
            shutil.copy(os.path.join(first, i), sec)
            print(f'+')
        else:
            print(f'-')