# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите любое число: ')
sum_number = 0
for num in number:
    if num.isdigit(): # мой вариант num != "," and num != "." and num != 0
        sum_number+=int(num)
print(f'{number} -> {sum_number}')
