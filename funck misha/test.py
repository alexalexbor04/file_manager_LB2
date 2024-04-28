import os

def del_folder(name):
    try:
        os.rmdir(name)
        print(f'Yes')
    except FileNotFoundError:
        print(f'No')
    except OSError:
        print(f'asd')