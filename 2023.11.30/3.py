n = abs(int(input('>Введите целое число: ')))
sum = n
for i in range(1, n//2 + 1):
        if n % i == 0:
            sum += i
print(sum)

# >Введите целое число: 50
# 93

# >Введите целое число: -50
# 93