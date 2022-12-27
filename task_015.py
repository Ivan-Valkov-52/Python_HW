# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

number = int(input('Введите число Фибоначчи = '))

my_fib = [0, 1]
my_negafib = [1]

for num in range(2, number+1):
    sum = my_fib[num-2] + my_fib[num-1]
    my_fib.append(sum)
    if num % 2 == 0:
        my_negafib.insert(0, -(sum))
    else:
        my_negafib.insert(0, sum)

print(f'{my_negafib + my_fib}')
