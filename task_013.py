# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def get_list(lengt_list):
    random_list = []
    for _ in range(lengt_list):
        random_list.append(round(random.uniform(0, lengt_list + 1), 2))
    return random_list

def fractional_part(my_list):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(round(my_list[i] % 1, 2))
    return new_list

get_lengt_list = int(input('Задайте длину списка: '))
my_list = get_list(get_lengt_list)
print(my_list)
difference = max(fractional_part(my_list)) - min(fractional_part(my_list))
print(round(difference, 2))