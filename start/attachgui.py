"""
Пример 1.26
В сценарии присоединяем наш графический интерфейс с одной кнопкой к
другому окну popup типа Toplevel, которое передается импортированному
приложению через вызов конструктора, как родительский компонент.
"""


from tkinter import *
from tkinter102 import MyGui

# главное окно приложения
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# окно диалога
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)     # присоединить наши виджеты
mainwin.mainloop()
