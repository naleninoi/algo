# Урок 3, задача №5
"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random

SIZE = 30
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

max_negative = MIN_ITEM

for i in array:
    if 0 > i > max_negative:
        max_negative = i

print(max_negative)
