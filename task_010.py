# Реализуйте алгоритм перемешивания списка.

from random import *

def sorting_list(my_list):
    for i in reversed(range(0, len(my_list)-1)):
        print(i, end=' ')
        j = randint(0, i + 1)
        my_list[i], my_list[j] = my_list[j], my_list[i]

number = int(input('Введите количество элементов списка: '))
my_list = []
for _ in range(number):
    my_list.append(randrange(10, 99))
print(my_list)
sorting_list(my_list)
print(my_list)
