import os
import shutil

def move_files_from_one_folder_to_another(first_dir, second_dir, files):
    
    if not os.path.isdir(first_dir) or not os.path.isdir(second_dir):
        print("\033[31m{}" .format("Обеих папок или одной из них не существует, укажите правильные названия"))
        return

    for file in files:
        moving_path = os.path.join(first_dir, file)

        if os.path.isfile(moving_path):
            shutil.move(moving_path, second_dir)
            print("\032[32m{}" .format(f'Файл {file} перемещкн из {first_dir} в {second_dir}'))        
        else:
            print("\031[31m{}" .format(f'Файла {file} нет в папке {first_dir}'))