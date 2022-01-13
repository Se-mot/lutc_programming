"""
Пример 1.3
Сценарий выполняет загрузку базы данных из файла.
Имя файла загружается при импортировании функции
"""
from make_db_file import loadDbase

db = loadDbase()
for key in db:
    print(key, '=>\n', db[key])
print(db['sue']['name'])
