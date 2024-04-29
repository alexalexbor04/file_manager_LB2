import os

def read_a_txt_file(txt_file_name):
    if os.path.isfile(txt_file_name):
        with open(txt_file_name, 'r') as file:
            print("\033[32m{}" .format(f'Содержание файла {txt_file_name}:'))
            print(file.read())

    else:
        print("\033[31m{}" .format(f'Файла {txt_file_name} не существует'))