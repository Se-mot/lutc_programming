# -*- coding: utf-8 -*-
"""
Пример 4.1
Процедура сканирования файлов
"""

def scaner(name, function):
    file = open(name, 'r')  # создать объект файла
    while True:
        line = file.readline()  # вызов метода файла
        if not line:
            break  # до конца файла
        function(line)  # вызвать объект функции
    file.close()
