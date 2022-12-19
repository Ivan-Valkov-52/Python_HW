# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

coordinate_xA = int(input('Введите координату х точки А: '))
coordinate_yA = int(input('Введите координату у точки А: '))
coordinate_xB = int(input('Введите координату х точки В: '))
coordinate_yB = int(input('Введите координату у точки В: '))
distance_AB = math.sqrt((coordinate_xB - coordinate_xA)** 2 + (coordinate_yB - coordinate_yA)**2)
print(f'A({coordinate_xA},{coordinate_yA}); B({coordinate_xB},{coordinate_yB}) -> {"%.3f" %distance_AB}')
