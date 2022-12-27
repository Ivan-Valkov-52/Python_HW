# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def get_list(lengt_list):
    random_list = []
    for _ in range(lengt_list):
        random_list.append(random.randrange(-lengt_list, lengt_list + 1))
    return random_list

my_list = get_list(4)
print(my_list)
print(f'Ответ: {sum(my_list[1::2])}')

