"""
Пример 5.1 (Только под Unix. Не запускается в Винде)
Ответвляет дочерние процессы, пока не нажата 'q'.
"""

import os


def child():
    print('Hello from child', os.getpid())
    os._exit(0)  # иначе возврат в "родительский --> внуки"


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break


parent()
