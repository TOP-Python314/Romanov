

# =============== 4 =============

number = int(input('Введите любое трехзначное число: '))
number_1 = number  // 100
number_2 = number % 100 // 10
number_3 = number % 10
# print('Сумма цифр = ', number_1 + number_2 + number_3, '\n' + 'Произведение цифр = ', number_1 * number_2 * number_3 )
print(f'Сумма цифр = {number_1 + number_2 + number_3}', f'Произведение цифр = {number_1 * number_2 * number_3}', sep = '\n')

# Ввод: 

    # Введите любое трехзначное число: 333

# Вывод:

    # Сумма цифр =  9
    # Произведение цифр =  27