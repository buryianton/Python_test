#Методы list: list.append(x), list.insert(i,x), list.pop([i]), list.copy(), list.count(x)
#Методы str: s.split(), s.lower(), s.swapcase(), s.isdigit(), s.isalnum()
#Методы set: set.union(), set.intersection(), set.difference(), set.symmetric_difference(), set.copy()
#Методы dict: dict.clear(), dict.copy(), dict.keys(), dict.pop(), dict.popitem()

"""
(МОДУЛЬ 1) Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
"""

numbers = int(input('Введите кол-во элементов: '))
our_list = []
for i in range(numbers):
   our_list.append(input('Введите число: '))

print(our_list)
