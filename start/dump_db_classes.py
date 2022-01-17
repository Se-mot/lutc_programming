"""
Пример 1.19
Сценарий читает содержимое хранилища и выводит значения полей записей
"""


import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n', db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())
