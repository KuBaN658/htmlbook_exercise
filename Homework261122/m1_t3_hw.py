"""
Задача №3
В подъезде №1 пятиэтажного жилого дома 15 квартир.
Определить, на каком этаже этого подъезда находится квартира с заданным номером.

Решить без использования if.

"""
# Ваш код
num_flat = int(input('Введите номер квартиры(1-15): '))
print(f'Квартира находится на {num_flat//3 + (num_flat % 3 != 0)} этаже')