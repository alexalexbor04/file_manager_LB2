import os
import shutil

def arch_files(files, name_of_new_archive):
    try:
        os.makedirs(name_of_new_archive)
        for file in files:
            shutil.move(file, os.path.join(name_of_new_archive, os.path.basename(file)))
        shutil.make_archive(name_of_new_archive, 'zip', name_of_new_archive)
        shutil.rmtree(name_of_new_archive)
        print("yest archiv")
    except:
        print("net archiva")