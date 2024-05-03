import os

from sasha_funcs.folder_config import folder_configuration
from func_misha.append_text import append_text
from func_misha.arch_files import arch_files
from func_misha.del_files import del_files
from func_misha.del_folder import del_folder
from func_misha.files_copying import files_copying
from func_misha.make_file import make_file
from func_misha.make_folder import make_folder
from sasha_funcs.unarchive_file import unarchive_file
from sasha_funcs.disk_space import disk_space
from sasha_funcs.move_files_from_one_fold_to_another import move_files_from_one_folder_to_another
from sasha_funcs.read_a_txt_file import read_a_txt_file
from sasha_funcs.rename_file import rename_file


def main():
    print('Меню (от 0 до 13):')
    folder = 'root_folder'
    folder_configuration(folder)

    while True:
        print("\n\033[37m{}" .format("0 - Завершить работу"))
        print('1 - Создать папку')
        print('2 - Удалить папку')
        print('3 - Переместиться между папками')
        print('4 - Создать пустой файл')
        print('5 - Записать текст в указанный файл')
        print('6 - Посмотреть содержание текстового файла')
        print('7 - Удалить указанный файл')
        print('8 - Копировать файл из одной папки в другую')
        print('9 - Переместить файл из одной папки в другую')
        print('10 - Изменить имя файла')
        print('11 - Заархивировать указанный файл')
        print('12 - Разархивировать указанный файл')
        print('13 - Вывести информацию о состоянии диска')
        print(f'\nВаше текущее положение - папка {folder}\n')

        opt = int(input('Выберите положение меню: '))
        while opt > 13 or opt < 0:
            opt = int(input('Выберите положение меню: '))


        match opt:
            case 0:
                print('Вы завершили работу программы.')
                break

            case 1:
                dir_name = input('Введите название папки для создания: ')
                make_folder(os.path.join(folder, dir_name))

            case 2:
                dir_name = input('Введите название папки, которую хотите удалить: ')
                del_folder(os.path.join(folder, dir_name))

            case 3:
                dir_name = input('Введите название папки, в которую хотите переместиться: ')

                if dir_name == '':
                    folder = 'root_folder'

                elif dir_name == '..':

                    if not os.path.samefile(folder, os.path.abspath('root_folder')):
                        folder = os.path.dirname(folder)
                    else:
                        print('Вы не можете перейти выше рабочей папки.')


                else:
                    if os.path.isdir(os.path.join(folder, dir_name)):
                        folder = os.path.join(folder, dir_name)

            case 4:
                file_name = input('Введите название файлов через запятую: ').split(', ')
                file_name = [os.path.join(folder, file) for file in file_name]
                make_file(file_name)

            case 5:
                file_name = input('Введите название файла для записи текста: ')
                text = input('Введите текст для добавления: ')
                append_text(os.path.join(folder, file_name), text)

            case 6:
                file_name = input('Введите название файла, содержимое которого необходимо прочитать: ')
                read_a_txt_file(os.path.join(folder, file_name))

            case 7:
                file_name = input('Введите название файлов через запятую: ').split(', ')
                file_name = [os.path.join(folder, file) for file in file_name]
                del_files(file_name)

            case 8:
                dir1 = input('Введите путь к исходной папке, где лежит файл: ')
                dir2 = input('Введите путь к папке, куда нужно скопировать данный файл: ')
                files = input('Введите название файлов через запятую: ').split(', ')
                files_copying(os.path.join(folder, dir1), os.path.join(folder, dir2), files)

            case 9:
                prev_dir = input('Введите путь к исходной папке, где лежит файл: ')
                next_dir = input('Введите путь к папке, куда необходмо переместить файл: ')
                files = input('Введите название файлов через запятую: ').split(', ')
                files = [os.path.join(folder, file) for file in files]
                move_files_from_one_folder_to_another(os.path.join(folder, prev_dir), os.path.join(folder, next_dir), files)

            case 10:
                prev_name = input('Введите текущее имя файла: ')
                next_name = input('Введите новое имя файла: ')
                rename_file(os.path.join(folder, prev_name), os.path.join(folder, next_name))
            
            case 11:
                files_arch = input('Введите название файлов, которые хотите добавить в архив, через запятую: ').split(', ')
                # files_arch = [os.path.join(folder, file) for file in files_arch]
                arch_name = input('Введите название архива: ') 
                arch_files(files_arch, os.path.join(folder, arch_name), folder)

            case 12:
                unarch = input('Введите название архива: ')
                dest = input('Введите название папки для разархивации: ')
                unarchive_file(unarch, dest)

            case 13:
                disk_space()           

main()