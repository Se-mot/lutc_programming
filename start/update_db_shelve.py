"""
Пример 1.13
Сценарий демонстрирует как изменять данные в хранилище shelve
"""
import shelve

from initdata import tom

db = shelve.open('people-shelve')
sue = db['sue']  # извлекаем объект sue
sue['pay'] *= 1.5
db['sue'] = sue  # изменяем объект sue
db['tom'] = tom  # добавляем новую запись
db.close()
