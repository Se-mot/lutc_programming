"""
Пример 1.28
В сценарии получаем ввод от пользователя с помощью виджета Entry
Инструкция lambda откладывает вызов функции reply.
В примере изменяем ярлык и текст в заголовке окна верхнего уровня.
"""


from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='Hello %s !' % name)


top = Tk()
top.title('Echo')
#top.iconbitmap('py-blue-trans-out.ico')

Label(top, text='Enter you name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()
