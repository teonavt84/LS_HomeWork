# Операция определяется символом:

# - возвращает остаток от деления второго числа на первое
# ! - возвращает число, у которого сумма цифр больше
# @ - возвращает большее число из двух
# $ - возвращает число, у которого больше цифр
# В случае если оба числа удовлетворяют условию, то возвращается первое.

# Примеры:

# 28#26379 => 3
# 1111!23 => 23
# 123@876 => 876
# 456$0007 => 0007
import re
while True:
    calc = input('Введите операцию: ')
    symbol_match = r'(\D)'
    symbol_search = re.search(symbol_match, calc)
    symbol_num_element = calc.find(symbol_search.group(1))
    symbol = symbol_search.group(1)
    left_side = calc[:symbol_num_element]
    right_side = calc[symbol_num_element+1:]
    if symbol == '#':
        remnant = int(right_side) % int(left_side)
        print(f'Остаток от деления второго числа на первое равен {int(right_side) % int(left_side)}')
    elif symbol == '!':
        summ_left = 0
        summ_right = 0
        for i in left_side:
            summ_left = summ_left + int(i)
        for i in right_side:
            summ_right = summ_right + int(i)
        if summ_left > summ_right:
            print(f'Число, у которого сумма цифр больше {left_side}')
        elif summ_left < summ_right:
            print(f'Число, у которого сумма цифр больше {right_side}')
        else:
            print('Сумма чисел равна.')
    elif symbol == '@':
        if int(left_side) > int(right_side):
            print(f'Большее число {left_side}')
        elif int(left_side) < int(right_side):
            print(f'Большее число {right_side}')
        else:
            print('Числа равны.')
    elif symbol == '$':
        if len(left_side) > len(right_side):
            print(f'У числа {left_side} больше цифр')
        elif len(left_side) < len(right_side):
            print(f'У числа {right_side} больше цифр')
        elif len(left_side) == len(right_side):
            print(f'У числа {left_side} больше цифр')
    else:
        print('Введены неверные данные.')
    repeat = input('Ввести данные повторно? Y/N: ')
    if repeat.capitalize() == 'Y':
        continue
    else:
        break
