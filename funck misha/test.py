import os

def append_text(imya, text):
    if os.path.isfile(imya):
        with open(imya, 'a') as file:
