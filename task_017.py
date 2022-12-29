# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from math import sqrt

def factors(number):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number /= 2
    for num in range(3, int(sqrt(number)) + 1, 2):
        while number % num == 0:
            factors.append(num)
            number /= num
    if number > 2:
        factors.append(int(number))
    return factors


number = int(input('Введите натуральное число N: '))
print(number, '=', ' x '.join(str(num) for num in factors(number)))
