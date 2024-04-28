import os

def make_folder(name):
    try:
        os.mkdir(name)
        print(f'oh yes')
    except:
        print(f'oh no')