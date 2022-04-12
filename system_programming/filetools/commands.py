#!/usr/local/bin/python
"""
Пример 4.2
Сценарий, выполняющий простое преобразование строк.
Импортируем функцию scaner из модуля scanfile
"""

from sys import argv

from scanfile import scaner


class UnknownCommand(Exception):
    pass


def processLine(line):  # определить функцию,
    if line[0] == '*':  # применяемую к каждой строке
        print('Ms.', line[1:-1])
    elif line[0] == '+':
        print('Mr.', line[1:-1])  # отбросить первый и последний символы
    else:
        raise UnknownCommand(line)  # возбудить исключение


filename = 'data.txt'
if len(argv) == 2:
    filename = argv[1]  # аргумент коммандной строки с
scaner(filename, processLine)  # именем файла запускает сканер
