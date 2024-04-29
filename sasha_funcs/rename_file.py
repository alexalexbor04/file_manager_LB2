import os

def rename_file(previous_name, next_name):
    if os.path.isfile(previous_name):
        os.rename(previous_name, next_name)
        print("\033[32m{}" .format(f'Файл {previous_name} сменил название на {next_name}'))

    else:
        print("\033[31m{}" .format(f'Файла {previous_name} не существует'))