mile = input('Введите целую часть миль: ')
mile_1 = input('Введите десятичную часть миль: ')
# ИСПРАВИТЬ: этот способ не сработает, если пользователю потребуется ввести дробную часть для числа с количеством десятичных знаков больше одного (см. тест ниже) — придумайте более универсальное решение
# ИСПОЛЬЗОВАТЬ везде: круглые скобки используются для литерала кортежа, изменения порядка вычисления выражений, вызова функций и записи составного выражения на нескольких строчках — больше нигде и никак
# ИСПРАВИТЬ: повторное вычисление одного и того же объекта неоптимально
print(f'{(mile + "." + mile_1)} миль = {round(float(mile + "." + mile_1) * 1.61, 1)} км')


# ИСПОЛЬЗОВАТЬ везде: достаточно копировать содержимое терминала как есть: без изменений, дополнительных комментариев, отступов и т.п.
# Введите целую часть миль: 15
# Введите десятичную часть миль: 7
# 15.7 миль = 25.3 км

# Введите целую часть миль: 5
# Введите десятичную часть миль: 81
# КОММЕНТАРИЙ: должно быть 5.81 миль
# 13.1 миль = 21.1 км


# ИТОГ: нужно лучше, доработать — 2/5
