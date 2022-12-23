# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input('Введите число N: '))
my_list = []
for num in range(1,number + 1):
    my_list.append(round((1 + 1/ num)**num, 2))
print(my_list)    
print(sum(my_list))