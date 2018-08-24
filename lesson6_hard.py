# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

class Igrushka:
    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
        print(self.name,self.color,self.type)


class Animals(Igrushka):
    def __init__(self, name, color, type):
        super().__init__(name, color, type)
        self.type = 'Animals'


class Multfilm(Igrushka):
    def __init__(self, name, color, type):
        super().__init__(name, color, type)
        self.type = 'Multfilm'


class Fabrika(Igrushka):
    def __init__(self, name, color, type):
        super().__init__(name, color, type)

    def SelectType(self, type):
        if type == 'Animals':
            return print(Animals)
        elif type == 'Multfilm':
            return print(Multfilm)

    def Zakup(self):
        print('Закуп сырья')

    def Poshiv(self):
        print('Пошив')

    def Okraska(self):
        print('Окраска')


game = Igrushka('Лошадка', 'Коричневая', 'Animals')
toy = Fabrika('Лошадка', 'Коричневая', 'Animals')
toy.SelectType('Animals')
