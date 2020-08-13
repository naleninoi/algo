# Урок 2, задача №8
"""
Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать,
задаются вводом с клавиатуры.
"""


# https://drive.google.com/file/d/1GT181Ddb1Aa7eHZa0Z7IvIQe6Mg5Nyww/view?usp=sharing

def counter(digit, num):
    count = 0
    while num > 0:
        m = num % 10
        if m == digit:
            count += 1
        num = num // 10
    return count


digit_total = 0

digit = int(input('Введите цифру от 0 до 9 - именно ее мы будем искать: '))
numbers = int(input('Введите количество чисел, в которых будем вести поиск: '))
for i in range(1, numbers + 1):
    num_search = int(input(f'Введите число №{i}: '))
    result = counter(digit, num_search)
    print(f'Цифра {digit} в этом числе встречается {result} раз')
    digit_total += result
print(f'Вы ввели {numbers} чисел. Цифра {digit} в них встретилась всего {digit_total} раз')
