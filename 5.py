# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*     негафибоначчи Fn = F(n+2)−F(n+1). фибоначчи Fn = F(n-1)+F(n-2)

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


number = int(input('введите значение для Фибоначчи '))
fibo = []

def fibo_posi(number):
    if number in (1,2):
        return 1
    elif number == 0:
        return 0
    return fibo_posi(number - 1) + fibo_posi(number - 2)

def fibo_neg(number):
    if number == 0:
        return 0
    elif number == -1:
        return 1
    return fibo_neg(number + 2) - fibo_neg(number + 1)

for i in range(-number, 0):
    fibo.append(fibo_neg(i))

for i in range(0, number + 1):
    fibo.append(fibo_posi(i))

print(fibo)