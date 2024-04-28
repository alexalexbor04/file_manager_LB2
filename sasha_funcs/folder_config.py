import os

def folder_configuration(folder):
    path = os.getcwd()
    if not os.path.exists(f'{path}/{folder}'):
        os.mkdir(f'{path}/{folder}')