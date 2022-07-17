# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


lst = [2,5,7,3,8,4,5,4]

def sum_negative_index(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            False
        else:
            sum += lst[i]
    return sum
print(sum_negative_index(lst))