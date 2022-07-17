# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5.567, 10.03] => 0.564 или 564

lst = [1.1, 1.7532, 3.1, 5.567, 10.03]

def max_min_diff(lst):
    #     max_index = int(str(lst[0]).split('.')[1])
    #     min_index = int(str(lst[0]).split('.')[1])

    #     for i in range(len(lst)):
    #         num_after_dot = int(str(lst[i]).split('.')[1])

    #         if min_index > num_after_dot:
    #             min_index = num_after_dot

    #         if max_index < num_after_dot:
    #             max_index = num_after_dot
    #     print(f"максимальное значение {max_index}, минимальное {min_index} \nразница между {max_index} и {min_index} = {max_index - min_index}")
    #
    #   решение не до конца проработанное, не знаю, как сделать, чтобы он считал 0 в числе 10.03

    lst = [round((i - int(i)), 3) for i in lst]
    print(f"Разница между {max(lst)} и {min(lst)} = {max(lst) - min(lst)}")

print(max_min_diff(lst))