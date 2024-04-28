import zipfile

def unarchive_file(archived_file, dest):
    try:
        with zipfile.ZipFile(archived_file, 'r') as zipf:
            zipf.extractall(dest)
        print(f"Файлы успешно разархивированы в '{dest}'.")
    except FileNotFoundError:
        print(f"Файл архива {archived_file} не найден.")