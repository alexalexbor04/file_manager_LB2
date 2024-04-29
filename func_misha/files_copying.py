import os
import shutil

def files_copying(first_folder, second_folder, files):
    if not os.path.isdir(first_folder) or not os.path.isdir(second_folder):
        print("\033[31m{}" .format('Такой(-их) папки нет'))
        return
    for file in files:
        if os.path.isfile(os.path.join(first_folder, file)):
            shutil.copy(os.path.join(first_folder, file), second_folder)
            print("\033[32m{}" .format(f'Файл успешно скопирован в {second_folder}'))
        else:
            print("\033[31m{}" .format(f'Файла {file} не существует'))