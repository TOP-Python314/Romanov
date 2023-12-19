nums = []
while True:
    number = int(input('Введите целое число: '))
    if number % 7 == 0:
        nums.append(str(number))
       
    else:
        if len(nums):
            print(f'{" ".join(nums[::-1])}')
        else: print('Список пуст')
        break  

# Введите целое число: 7
# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 1
# 21 14 7    
    
# Введите целое число: 1
# Список пуст