# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

def degree_number(number):
    degree = 0
    while number != 1:
        number *= 10
        degree += 1
    return degree

round_number = float(input('Введите число d с точностью 10^{-1} ≤ d ≤10^{-10}: '))
flag = True
while flag:
    if 10**(-10) <= round_number <= 10**(-1):
        flag = False
    else:
        round_number = float(input('Попробуйте ещё раз:'))

print(f'π = {pi}')
print(f'При d = {round_number}, π = {round(pi, degree_number(round_number))}')