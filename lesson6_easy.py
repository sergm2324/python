# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self):
        self.speed = 60
        self.color = 'красный'
        self.name = 'Городская машина'
        self.is_police = False

    def go(self):
        print('Машина ' + self.name + ' поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина ' + self.name + ' повернула направо')
        elif direction == 'left':
            print('Машина ' + self.name + ' повернула налево')

class SportCar:
    def __init__(self):
        self.speed = 120
        self.color = 'красный'
        self.name = 'Спортивная машина'
        self.is_police = False

    def go(self):
        print('Машина ' + self.name + ' поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина ' + self.name + ' повернула направо')
        elif direction == 'left':
            print('Машина ' + self.name + ' повернула налево')

class WorkCar:
    def __init__(self):
        self.speed = 20
        self.color = 'красный'
        self.name = 'Рабочая машина'
        self.is_police = False

    def go(self):
        print('Машина ' + self.name + ' поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина ' + self.name + ' повернула направо')
        elif direction == 'left':
            print('Машина ' + self.name + ' повернула налево')


class PoliceCar:
    def __init__(self):
        self.speed = 150
        self.color = 'красный'
        self.name = 'Полицейская машина'
        self.is_police = True

    def go(self):
        print('Машина ' + self.name + ' поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина ' + self.name + ' повернула направо')
        elif direction == 'left':
            print('Машина ' + self.name + ' повернула налево')



# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class AllCar:
    def __init__(self):
        self.speed = 60
        self.color = 'красный'
        self.name = 'Городская машина'
        self.is_police = False

    def go(self):
        print('Машина ' + self.name + ' поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        if direction == 'right':
            print('Машина ' + self.name + ' повернула направо')
        elif direction == 'left':
            print('Машина ' + self.name + ' повернула налево')


class SportCar(AllCar):
    def __init__(self):
        super().__init__()
        self.name = 'Спортивная машина'
        self.speed = 120


class WorkCar(AllCar):
    def __init__(self):
        super().__init__()
        self.name = 'Рабочая машина'
        self.speed = 20


class PoliceCar(AllCar):
    def __init__(self):
        super().__init__()
        self.name = 'Полицейская машина'
        self.speed = 150
        self.is_police = True


mycar = TownCar()
mycar.go()
print(mycar.name)
mycar.turn('left')
print(mycar.is_police)
mycar2 = PoliceCar()
mycar2.go()
print(mycar2.name)
print(mycar2.speed)

