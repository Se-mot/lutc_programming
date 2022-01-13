"""
Пример 1.12
Сценарий повторно открывает хранилище и извлекает хранящиеся в нем записи.
Обращаемся к тому же имени для бд.
"""
import shelve

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
db.close()
