"""
Пример 1.27
За счет механизма наследования изменяем реализацию метода reply
"""


from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui


class CustomGui(MyGui):     # наследует __init__
    def reply(self):        # замещает reply
        showinfo(title='popup', message='Ouch')


if __name__ == '__main__':
    CustomGui().pack()
    mainloop()
