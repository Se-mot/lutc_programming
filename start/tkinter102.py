"""
Пример 1.25
Сценарий с графическим интерфейсом - добавлена 1 кнопка.
Реализован в виде класса(подкласса Frame)
Frame - виджет - контейнер для других виджетов
Такая реализация --> наш графический интерфейс автоматически становится
присоединяемым компонентом - т.е. мы можем добавлять все
виджеты создаваемые этим классом в любой другой графический интерфейс
См следующий пример
"""


from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
