# ============= 4 =============

xy = input('Введите координаты: ')
xy1 = input('Введите координаты: ')

if 'a' <= xy[0] <= 'h' and 1 <= int(xy[1]) <= 8:
    
    if 'a' <= xy1[0] <= 'h' and 1 <= int(xy1[1]) <= 8:
    
        if (((ord(xy[0]) + int(xy[1])) % 2 == 0) and ((ord(xy1[0]) + int(xy1[1])) % 2 == 0)):
            print('да')
        elif (((ord(xy[0]) + int(xy[1])) % 2 != 0) and ((ord(xy1[0]) + int(xy1[1])) % 2 != 0)):
            print('да')
        else: 
            print('нет')
    else:
        print('неверные координаты')

else:
    print('неверные координаты')






# Ввод:
    # Введите координаты: a2
    # Введите координаты: d3

# Вывод:

    # да

# Ввод:
    # Введите координаты: a1
    # Введите координаты: a2

# Вывод:

    # нет

# Ввод:
    #Введите координаты: a1
    #Введите координаты: n9
# Вывод:
    # неверные координаты