number = int(input('Введите любое трехзначное число: '))
number_1 = number  // 100
number_2 = number % 100 // 10
number_3 = number % 10
# print('Сумма цифр = ', number_1 + number_2 + number_3, '\n' + 'Произведение цифр = ', number_1 * number_2 * number_3 )
print(
    # ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует записывать длинные аргументы или большое количество аргументов на нескольких строчках
    f'Сумма цифр = {number_1 + number_2 + number_3}',
    f'Произведение цифр = {number_1 * number_2 * number_3}',
    # ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует добавлять пробелы вокруг = при передаче аргументов по ключу
    sep='\n'
)


# ИСПОЛЬЗОВАТЬ везде: достаточно копировать содержимое терминала как есть: без изменений, дополнительных комментариев, отступов и т.п.
# Введите любое трехзначное число: 333
# Сумма цифр =  9
# Произведение цифр =  27

