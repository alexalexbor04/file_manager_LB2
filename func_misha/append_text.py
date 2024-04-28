import os

def append_text(name, text):
    if os.path.isfile(name):
        with open(name, 'a') as file:
            if file.tell() > 0:
                file.write('\n')
            file.write(text)
            print(f'Добавление текста в файл\n...\n...\nГотово.')    
    else:
        print(f'Указанный файл не существует')