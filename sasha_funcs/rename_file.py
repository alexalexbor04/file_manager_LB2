import os

def rename_file(previous_name, next_name):
    if os.path.isfile(previous_name):
        os.rename(previous_name, next_name)
        print(f'Файл {previous_name} сменил название на {next_name}')

    else:
        print(f'Файла {previous_name} не существует')