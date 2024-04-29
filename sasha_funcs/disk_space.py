import shutil

def disk_space():
    total, used, free = shutil.disk_usage(".")
    print("\033[35m{}" .format(f"Общий объем диска: {total / (2**30):.2f} GB"))
    print("\033[35m{}" .format(f"Использовано: {used / (2**30):.2f} GB"))
    print("\033[35m{}" .format(f"Свободно: {free / (2**30):.2f} GB"))