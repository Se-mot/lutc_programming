"""
Пример 5.3
(в Windows не запускается)
Запускает программы, пока не нажата q
"""

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid == 0:
        os.execlp('python', 'python', 'child.py', str(parm))
            # копия процесса, подменить программу
        assert False, 'error starting program'   # возврата быть не должно

    else:
        print('Child is', pid)
        if input() == 'q':
            break