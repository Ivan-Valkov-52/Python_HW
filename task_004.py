# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Введите номер четверти: "))
match quarter_number:
    case 1:
        print('X > 0 and Y > 0')
    case 2:
        print('X < 0 and Y > 0')
    case 3:
        print('X < 0 and Y < 0')
    case 4:
        print('X > 0 and Y < 0')
    case _:
        print('Нет такой четверти!')