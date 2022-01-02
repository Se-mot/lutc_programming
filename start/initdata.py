# инициализировать данные для последующего сохраения в файлах

# записи
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dav'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}

# база данных
db = {'bob': bob, 'sue': sue, 'tom': tom}

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n', db[key])
