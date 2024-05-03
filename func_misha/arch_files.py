import os
import shutil
from sasha_funcs.move_files_from_one_fold_to_another import move_files_from_one_folder_to_another

def arch_files(files, name_of_new_archive, folder):
    try:
        os.mkdir(name_of_new_archive)
        move_files_from_one_folder_to_another(folder, name_of_new_archive, files)
        shutil.make_archive(name_of_new_archive,'zip', name_of_new_archive)
        shutil.rmtree(name_of_new_archive)
        print("\033[32m{}" .format(f"{name_of_new_archive}.zip успешно создан"))
    except:
        print("\033[31m{}" .format("Ошибка при создании архива"))