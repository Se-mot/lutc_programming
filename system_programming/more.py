"""
Пример 2.1
Вспомогательный сценарий.
Разбивает строку или текстовый файл на страницы для интерактивного просмотра
"""


def more(text, numlines=15):
    lines = text.splitlines()  # подобно split('\n) но без '' в конце
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and input('More?') not in ['y', 'Y']:
            break
#print('Hello boy')

if __name__ == '__main__':
    import sys
    print('Hello __main__ more.py')
    if len(sys.argv) == 1:  # вывести данные из stdin, если нет аргументов
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())  # отобразить постранично содержимое файла,
    # указанного в командной строке
