# Урок 3, задача №6
"""
В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

# генерация списка из случайных целых чисел

import random

SIZE = 50
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

min_number = MAX_ITEM
max_number = MIN_ITEM

# определение максимального и минимального элементов в списке

for i in array:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i

# определение позиций макс. и мин. элементов
# определение начальной и конечной позиции последовательности между макс. и мин. эл-тами

pos_max = array.index(max_number)
pos_min = array.index(min_number)
if pos_max > pos_min:
    start = pos_min
    finish = pos_max
else:
    start = pos_max
    finish = pos_min

# суммирование элементов в последовательности между макс. и мин. эл-тами
sum_ = 0
for i in range(start + 1, finish):
    sum_ += array[i]
    print(i)

print(sum_)
