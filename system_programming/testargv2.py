"""
Пример 3.2
Собирает параметры командной строки в словаре
"""


def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':  # поиск пар "-name value
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts


if __name__ == '__main__':
    from sys import argv  # пример клиентского кода

    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    print(myargs)
