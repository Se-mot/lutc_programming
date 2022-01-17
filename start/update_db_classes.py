"""
Пример 1.20
В сценарии происходит изменение информации в
сохраненной базе данных, но используются атрибуты экземпляров
"""

import shelve
db = shelve.open('class-shelve')

sue = db['sue']
sue.giveRaise(.20)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom
db.close()
