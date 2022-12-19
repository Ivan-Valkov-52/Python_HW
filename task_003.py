# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinate_x = int(input('Введите координату х: '))
coordinate_y = int(input('Введите координату у: '))
if coordinate_x != 0 or coordinate_y != 0:
    if coordinate_x > 0:
        if coordinate_y > 0:
            print(f'{coordinate_x}; {coordinate_y} -> 1')
        else: 
            print(f'{coordinate_x}; {coordinate_y} -> 4')
    else:
        if coordinate_y > 0:
            print(f'{coordinate_x}; {coordinate_y} -> 2')
        else:
            print(f'{coordinate_x}; {coordinate_y} -> 3')
else:
    print(f'{coordinate_x}; {coordinate_y} -> не могут быть одновременно равны 0!')
