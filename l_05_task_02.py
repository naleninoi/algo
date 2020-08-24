# Урок 5, задача №2

# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой
# — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


# функция добавляет нули в начало deque, пока длина deque не будет равна length
def add_zeros(line, length):
    for i in range(length - len(line)):
        line.appendleft('0')
    return line

# словари для перевода цифр между 10-чной и 16-чной системами
hex_to_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15}
dec_to_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
              13: 'D', 14: 'E', 15: 'F'}

# ввод двух 16-чных чисел. Приведение чисел к одной длине
num_1 = deque(input('Введите первое 16-ричное число: '))
num_2 = deque(input('Введите второе 16-ричное число: '))
length = max(len(num_1), len(num_2))
add_zeros(num_1, length)
add_zeros(num_2, length)

# перебор чисел в обратном порядке. перевод цифр из 16-чной в 10-чную систему.
# сложение цифр одного порядка. перевод результата обратно в 16-чную систему.
result = deque()
bonus = 0
for i in range(length - 1, -1, -1):
    digit_1 = hex_to_dec[(num_1[i])]
    digit_2 = hex_to_dec[(num_2[i])]
    sum_ = digit_1 + digit_2 + bonus
    if sum_ < 16:
        digit_hex = dec_to_hex[sum_]
        bonus = 0
    else:
        digit_hex = dec_to_hex[sum_ - 16]
        bonus = 1
    result.appendleft(digit_hex)
    if i == 0 and bonus == 1:
        result.appendleft('1')

# вывод результата
print(f"{''.join(num_1)} + {''.join(num_2)} = {''.join(result)}")
