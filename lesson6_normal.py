# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self):
        self.health = 100
        self.damage = 50
        self.armor = 0.7

    def _calculate_damage(self, damage, armor):
        return damage // armor


class Player(Person):
    def __init__(self):
        super().__init__()

    def attack(self):
        damage = self._calculate_damage(self.player['damage'], self.enemy['armor'])
        self.enemy['health'] -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self.player['name'], self.enemy['name'], damage,
                                                                        self.enemy['health']))


class Enemy(Person):
    def __init__(self):
        super().__init__()

    def attack(self):
        damage = self._calculate_damage(self.enemy['damage'], self.player['armor'])
        self.player['health'] -= damage
        print('{} нанес {} урона {}, у того осталось {} жизней.'.format(self.enemy['name'], self.player['name'], damage,
                                                                        self.player['health']))


class StartGame(Person):
    def __init__(self):
        super().__init__()

    def generate_name(self):
        self.player = {'name': input('Введите имя1: '), 'health': self.health, 'damage': self.damage,
                       'armor': self.armor}
        print('Player: ', self.player)
        self.enemy = {'name': input('Введите имя2: '), 'health': self.health, 'damage': self.damage,
                      'armor': self.armor}
        print('Enemy: ', self.enemy)

    def start(self):
        # Запоминаем кто последний атаковал
        last_attacker = self.player
        while self.player['health'] > 0 and self.enemy['health'] > 0:
            if last_attacker == self.player:
                Enemy.attack(self)
                last_attacker = self.enemy
            else:
                Player.attack(self)
                last_attacker = self.player

        if self.player['health'] > 0:
            print('Игрок победил!')
        else:
            print('Враг победил!')


player = StartGame()
player.generate_name()
player.start()
