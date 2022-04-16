"""
Пример 5.2
(Unix
Windows  -  запуск через os.spawn или multiprocessing
Основы ветвления: запустить 5 копий программы параллельно оригиналу;
каждая копия считает до пяти и выводит счетчик в тот же поток stdout --
при ветвлении процесса копируется память процесса, в т.ч. дескрипторы
файлов.
"""

import os
import time


def counter(count):  # вызывается в новом процессе
    for i in range(count):
        time.sleep(1)  # имитировать работу
        print('[%s] => %s' % (os.getpid(), i))


for i in range(5):
    pid = os.fork()
    if pid != 0:  # в родительском процессе
        print('Process %d spawned' % pid)  # продолжить цикл
    else:
        counter(5)  # в дочернем процессе
        os._exit(0)  # вызвать функцию и завершиться

print('Main process exiting')   # Родитель не должен ждать
