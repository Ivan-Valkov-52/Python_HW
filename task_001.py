# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week = input('Введите день недели: ')
match day_week:
    case '1' | '2' | '3' | '4'|'5':
        print(f'{day_week} -> нет')
    case '6' | '7':
        print(f'{day_week} -> Да')
    case _:
        print('Введены не корректные данные. Попробуйте ещё раз!')
