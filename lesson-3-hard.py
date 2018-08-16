# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import os

def attack(person1, person2, uron):
    if person1 == 1:
        enemy['health'] = float(enemy['health']) - uron
    else:
        player['health'] = float(player['health']) - uron


uron = lambda damage, armor: float(damage) / float(armor)


def savefile(path, **slovar):
    with open(path, 'w+', encoding='UTF-8') as file:
        for key, value in slovar.items():
            file.write('{}:{}\n'.format(key, value))
    file.close()


def readfile(path):
    d = {}
    with open(path, 'r', encoding='UTF-8') as file:
        for line in file:
            key, value = line.strip().split(':')
            d[key] = value
    file.close()
    return d


player = {'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'health': 100, 'damage': 50, 'armor': 1.2}

player['name'] = str(input('Введите имя 1 игрока: '))
enemy['name'] = str(input('Введите имя 2 игрока: '))
print('Ситуация до начала игры: \n' + '1 игрок: \n ' + str(player) + '\n' + '2 игрок: \n ' + str(enemy))

path_player = os.path.join('D:\Обучение_СП\GeekBrains\Lesson3_python', str(player['name']).lower() + '.txt')
path_enemy = os.path.join('D:\Обучение_СП\GeekBrains\Lesson3_python', str(enemy['name']).lower() + '.txt')

savefile(path_player, **player)
savefile(path_enemy, **enemy)
player = readfile(path_player)
enemy = readfile(path_enemy)


while float(player['health']) > 0 and float(enemy['health']) > 0:
    att_player = int(input('Введите номер атакующего игрока: '))

    if att_player == 1:
        att_enemy = 2
        uronmy = uron(player['damage'], player['armor'])
    else:
        att_enemy = 1
        uronmy = uron(enemy['damage'], enemy['armor'])

    attack(att_player, att_enemy, uronmy)

    if float(player['health']) <= 0:
        print('Победил игрок 2: \n' + '1 игрок: \n ' + str(player) + '\n' + '2 игрок: \n ' + str(enemy))
    elif float(enemy['health']) <= 0:
        print('Победил игрок 1: \n' + '1 игрок: \n ' + str(player) + '\n' + '2 игрок: \n ' + str(enemy))

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt

# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
