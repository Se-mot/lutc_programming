"""
Пример 1.6
В примере реализован доступ к сохраненной базе данных
peaple-pickle. Модуль pickle восстанавливает объект из
последовательного представления.
"""
import pickle
dbfile = open('people-pickle', 'rb')    #Двоичный режим работы
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
