# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def get_list(lengt_list):
    random_list = []
    for _ in range(lengt_list):
        random_list.append(random.randrange(-lengt_list, lengt_list + 1))
    return random_list

get_lengt_list = int(input('Задайте длину списка: '))
my_list = get_list(get_lengt_list)
print(my_list, end=' => ')
for i in range(round(len(my_list)//2) if len(my_list) % 2 == 0 else round(len(my_list)//2) + 1):
    print(my_list[i] * my_list[len(my_list) - 1 - i], end=', ')
