# Урок 3, задача №1
"""
В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

numbers = [i for i in range(2, 10)]
RANGE_START = 2
RANGE_END = 99

print(f'В диапазоне от {RANGE_START} до {RANGE_END}, чисел:')

for number in numbers:
    counter = 0
    for i in range(RANGE_START, RANGE_END):
        if i % number == 0:
            counter += 1
    print(f'кратных {number} - {counter}')
