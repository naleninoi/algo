# Урок 7, задача №2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)


def merge_sort_asc(arr, left_index, right_index):
    # Функция делит входной массив на 2 половины
    # и рекурсивно сортирует его
    if left_index >= right_index:
        return
    middle = (left_index + right_index) // 2
    merge_sort_asc(arr, left_index, middle)
    merge_sort_asc(arr, middle + 1, right_index)
    merge_arrays(arr, left_index, right_index, middle)


def merge_arrays(arr, left_index, right_index, middle):
    # Функция выполняет слияние двух массивов в один,
    # при этом сортирует их элементы по возрастанию

    # создаются копии входного массива
    left_copy = arr[left_index:middle + 1]
    right_copy = arr[middle + 1:right_index + 1]

    # начальные значения счетчиков для продвижения по массивам
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # обход массивов, пока в одном из них не закончатся элементы
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        # если в массиве left_copy содержится меньший элемент,
        # он помещается в отсортированный массив,
        # счетчик продвижения по саммиву left_copy увеличивается на 1
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        # в противном случае происходит выбор элемента и
        # продвижение по массиву right_copy
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        # в любом случае счетчик продвижения по
        # отсортированному массиву увеличивается на 1
        sorted_index += 1

    # если раньше закончились элементы в массиве right_copy,
    # в отсортированный массив добавляются оставшиеся элементы из left_copy
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1
    # если раньше закончились элементы в массиве left_copy,
    # в отсортированный массив добавляются оставшиеся элементы из right_copy
    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1


merge_sort_asc(array, 0, len(array) - 1)
print(array)
