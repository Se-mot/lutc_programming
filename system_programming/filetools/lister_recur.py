# -*- coding: utf-8 -*-
"""
Пример 4.5
Выводит список файлов в дереве каталогов с помощью рекурсии
"""

import os
import sys


def mylister(currdir):
    print('[' + currdir + ']')
    for file in os.listdir(currdir):  # генерирует список файлов
        path = os.path.join(currdir, file)  # добавить путь к каталогу
        if not os.path.isdir(path):  # нулевой случай рекурсии
            print(path)  # path - не директория -> печать
        else:
            mylister(path)  # рекурсивный спуск


if __name__ == '__main__':
    if len(sys.argv) == 1:
        mylister('.')
    else:
        mylister(sys.argv[1])  # имя каталога в коммандной строке
