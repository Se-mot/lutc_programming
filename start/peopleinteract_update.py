"""
Пример 1.22
Сценарий для заданного ключа позволяет ввести значения для каждого из
полей и либо изменяет существующую запись, либо созлает новую,
после чего сохраняет её с указанным ключом.
"""

# интерактивные изменения
import shelve

from person import Person

fieldnames = ('name', 'age', 'job', 'pay',)

db = shelve.open('class-shelve')
while True:
    key = input('\nKey? => ')
    if not key: break
    if key in db:
        record = db[key]  # изменить существующую или создать новую запись
    else:
        record = Person(name='?', age='?')  # для eval: строки  в кавычках
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\tnew?=>' % (field, currval))
        if newtext:
            setattr(record, field, eval(newtext))
    db[key] = record
db.close()
