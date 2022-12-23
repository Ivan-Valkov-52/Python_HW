# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
#  factorial()

def factorial_number(number):
    if number < 2:
        return 1
    else:
        return number * factorial_number(number - 1)


number = int(input('Введите число N: '))
my_list = []
for num in range(1, number + 1):
    my_list.append(factorial_number(num))
print(my_list)
