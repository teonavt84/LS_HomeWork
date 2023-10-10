# Посчитать количество символов равных значению переменной template
letters = 'Who keeps company with the wolf, will learn to howl.'
template = 'w'
count_symbols = 0
for element in letters:
    if element == template:
        count_symbols += 1
print(f'Количество символов {template} равно {count_symbols}')
