"""
Пример 1.5
Пример использования модуля pickle для сохранения записи в файл.
Запуск сценария сохраняет базу данных в файл с именем people-pickle
"""
import pickle

from initdata import db

dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
