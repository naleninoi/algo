# Урок 7, задача №3
# Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# # Примечание: задачу можно решить без сортировки
# исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался
# на уроках (сортировка слиянием также недопустима).

import random

M = 5
SIZE = 2 * M + 1
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)


def shaker_sort(arr):
    # функция сортирует массив методом шейкера
    last_ind = range(len(arr) - 1)
    change = True
    while change:
        for indices in (last_ind, reversed(last_ind)):
            change = False
            for i in indices:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    change = True
    return arr


def median(arr):
    # функция сортирует массив методом шейкера (вызывает функцию shaker_sort)
    # и возвращает медиану массива
    mid_ind = len(arr) // 2
    med = shaker_sort(arr)[mid_ind]
    return med


print(f'Медианой в массиве является: {median(array)}')
