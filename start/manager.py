"""
Пример 1.16
В примере специализируем класс Person через механизм наследование
"""


from person import Person


class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.2)
    print(tom.pay)
