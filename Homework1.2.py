# Вывести все символы, не равные значению exclude
letters = 'Who keeps company with the wolf, will learn to howl.'
exclude = 'l'
for element in letters:
    if element != exclude:
        print(element, end='')