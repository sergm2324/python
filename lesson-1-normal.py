# Задача: используя цикл запрашивайте у пользователя число пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число не верное,
# и сообщаете об диапазоне допустимых. И просите ввести заново.
# Допустим пользователь ввел 2, оно подходит, возводим в степень 2, и выводим 4

number = 100
while number < 0 or number >= 10:
    number = int(input('Введите число от 0 до 9: '))
    if number < 0 or number >= 10:
        print('Число неверное')
    else:
        print('Результат возведения в степень 2: ', number ** 2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
print(a, b)

a = a + b
b = a - b
a = a - b

print(a, b)
