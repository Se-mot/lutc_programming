"""
Пример 1.4
Сценарий загружает базу ланных, вносит изменения в неё и
сохраняет её обратно в файл.
Имя файла загружается при импортировании функции из модуля.
"""
from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
storeDbase(db)
