"""
Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""

first_list = input('Введите элементы 1-ого списка: ')
first_numbers = first_list.split(',')
second_list = input('Введите элементы 2-ого списка: ')
second_numbers = second_list.split(',')

print(first_numbers)
print(second_numbers)

for number in first_numbers.copy():
    if number in second_numbers:
        first_numbers.remove(number)

print(first_numbers)