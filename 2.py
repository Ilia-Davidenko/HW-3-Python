# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


import math


lst = [2,5,2,6,3]

def sum_first_last(lst):
    lenght_lst = len(lst)
    sum_lst = []
    # if lenght_lst % 2 == 0:
    for i in range(0, math.ceil(lenght_lst/2)):
        sum_index = 0
        sum_index = lst[i] * lst[lenght_lst - i - 1]
        sum_lst.append(sum_index)
    # else:
    #     for i in range(int(lenght_lst/2 + 1)):
    #         sum_index = 0
    #         sum_index = lst[i] * lst[lenght_lst - i - 1]
    #         sum_lst.append(sum_index)
    return sum_lst
print(sum_first_last(lst))