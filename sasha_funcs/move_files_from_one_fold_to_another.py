import os
import shutil

def move_files_from_one_folder_to_another(first_dir, second_dir, files):
    
    if not os.path.isdir(first_dir) or not os.path.isdir(second_dir):
        print("Такой папки нет")
        return

    for file in files:
        sourFile = os.path.join(first_dir, file)

        if os.path.isfile(sourFile):
            shutil.move(sourFile, second_dir)
            print(f'Расположение "{file}" изменено с "{first_dir}" на "{second_dir}"')
        else:
            print(f'Файла "{file}" нет в "{first_dir}"')