# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import *


def file_positions(number):
    with open('file.txt', 'w') as data:
        data.write(f'{randrange(1, number+1)}\n')
        data.write(f'{randrange(1, number+1)}')


number = int(input('Введите число: '))
my_list = []
for _ in range(number):
    my_list.append(randint(-number, number))
print(my_list)
value_numbers = 1
file_positions(number)
data = open('file.txt', 'r')
for item in data:
    print(f'Позиция №{int(item)}')
    value_numbers *= my_list[int(item) - 1]
data.close()
print(value_numbers)
