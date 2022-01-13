"""
Пример 1.11
Сохраняем объект из словаря в хранилище, созданном с помощью shelve
В каталоге создаем один или более файлов имена которых начинаются с people-shelve
Эти файлы составляют базу данных
"""
from initdata import bob, sue
import shelve
db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue
db.close()
