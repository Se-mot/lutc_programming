"""
Пример 3.5
Пример перенаправления стандартного потока вывода
Сценарий читает числа до символа конца файла и выводит их квадраты
"""


def interact():
    print('Hello stream world')    # print выводит в sys.stdout
    while True:
        try:
            reply = input('Enter a number>')    # input читает из sys.stdin
        except EOFError:
            break       # исключение при встрече символа EOF
        else:
            num = int(reply)
            print('%d squared is %d' % (num, num ** 2))
    print('Bye')


if __name__ == '__main__':
    interact()      # если выполняется а не импортируется
