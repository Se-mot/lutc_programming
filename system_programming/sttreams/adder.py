"""
Пример 3.7
Сценарий складывает строки с числами поступающие через стандартный поток ввода
"""


# import sys
sum = 0
while True:
    try:
        line = input()  # или sys.stdin.readlines()
    except EOFError:    # или for line in sys.stdin:
        break           # input отсекает символы \n в конце строк
    else:
        sum += int(line)
print(sum)
