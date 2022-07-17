# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec_number = int(input('введите число '))

def bi(dec_number):
    bi_number = ''
    while dec_number > 0:
        bi_number = bi_number + str(dec_number % 2)
        dec_number = dec_number // 2
        # if (dec_number == 0 or dec_number == 1):
        # bi_number = bi_number + str(dec_number)
            # break
    return bi_number[::-1]
print(f'десятичное число {dec_number} в двоичной системе = {bi(dec_number)}')