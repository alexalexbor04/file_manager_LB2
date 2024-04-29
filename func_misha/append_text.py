import os

def append_text(name, text):
    if os.path.isfile(name):
        with open(name, 'a') as file:
            if file.tell() > 0:
                file.write('\n')
            file.write(text)
            print("\033[32m{}" .format(f'Добавление текста в файл\n...\n...\nГотово.'))    
    else:
        print("\033[31m{}" .format(f'Указанного файла не существует'))