# Урок 2, задача №4
"""
Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


# https://drive.google.com/file/d/1GT181Ddb1Aa7eHZa0Z7IvIQe6Mg5Nyww/view?usp=sharing

def rec(count, base_num):
    if count <= 1:
        return base_num
    else:
        return base_num + rec(count - 1, base_num * -0.5)


base_num = 1
n = int(input('Введите натуральное число N: '))
result = rec(n, base_num)
print(result)
