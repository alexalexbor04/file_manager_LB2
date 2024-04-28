import shutil

def disk_space():
    total, used, free = shutil.disk_usage(".")
    print(f"Общий объем диска: {total / (2**30):.2f} GB")
    print(f"Использовано: {used / (2**30):.2f} GB")
    print(f"Свободно: {free / (2**30):.2f} GB")