"""
Пример 3.6
Сценарий сортирует строки с числами поступающие в стандартный
поток ввода
"""

import sys  # или sorted(sys.stdin)

lines = sys.stdin.readlines()  # читает входные строки
lines.sort()  # сортирует их
for line in lines:
    print(line, end='')  # отправляет результаты в stdout
    # для дальнейшей обработки
