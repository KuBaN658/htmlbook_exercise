"""
Задача №5

Вход:
    расстояние(50 - 10000 км),
    расход в литрах (5-25 литров) на 100 км и
    стоимость бензина(константа) = 52 руб

Выход:
    Проверка данных.
    Стоимость поездки в рублях и копейках как float()
    Используем функцию round()

Пример вывода результата:
Стоимость поездки: 1234.67 руб
"""
price = 52
distance = int(input('Введите расстояние поездки(50 - 10 000 км): '))
if 50 <= distance <= 10000:
    consumption = float(
        input('Введите расход бензина на 100 км(5.0 - 25.0 литров): '))
    if 5 <= consumption <= 25:
        cost = distance / 100 * consumption * price
        cost = round(cost, 2)
        print(f'Стоимость поездки: {cost} руб')
    elif consumption < 5:
        print('расход должен быть не менее 5 литров.')
    else:
        print('расход должен быть менее 25 литров.')
elif distance < 50:
    print('расстояние должно быть не менее 50 км.')
else:
    print('расстояние должно быть менее 10 000 км')