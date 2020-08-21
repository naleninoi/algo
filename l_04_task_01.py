# Урок 4, задача №1

# Проанализировать скорость и сложность одного
# любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.

# для анализа выбрана задача №2 к уроку 3 -
# во втором массиве сохранить индексы четных элементов первого массива.


import random, timeit, cProfile

SIZE = 1000
MIN_ITEM = -100
MAX_ITEM = 100
input_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# АЛГОРИТМ № 1 - ГЕНЕРАТОР СПИСКА ИЗ ИНДЕКСОВ ЧЕТНЫХ ЭЛЕМЕНТОВ
def evens_gen(array):
    result = [i for i in range(len(array)) if array[i] % 2 == 0]
    return result


# АЛГОРИТМ № 2 - ОБХОД СПИСКА ЦИКЛОМ FOR IN,
# ЗАПИСЬ ИНДЕКСОВ ВЫБРАННЫХ ЭЛЕМЕНТОВ В НОВЫЙ СПИСОК
def evens_cyc(array):
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result.append(i)
    return result


# АЛГОРИТМ № 3 - С СОХРАНЕНИЕМ ЧЕТНЫХ ЭЛЕМЕНТОВ В СЛОВАРЕ
def evens_dic(array):
    spam = {}
    result = []
    for i, item in enumerate(array):
        if item % 2 == 0:
            spam[i] = item
    for key in spam:
        result.append(key)
    return result


print(timeit.timeit('output_array = evens_gen(input_array)', number=100, globals=globals()))
print(timeit.timeit('output_array = evens_cyc(input_array)', number=100, globals=globals()))
print(timeit.timeit('output_array = evens_dic(input_array)', number=100, globals=globals()))

# при N (input array size) = 100
# 0.003623911999966367
# 0.0042351739998593985
# 0.005255014000340452

# при N = 500
# 0.01665890499998568
# 0.021571404000042094
# 0.025758551000308216

# при N = 1000
# 0.03298411200012197
# 0.04219196299982286
# 0.0523381809998682

# при N = 10000
# 0.3059099739998601
# 0.38653830800012656
# 0.5155204480001885

# при N = 1000000
cProfile.run('output_array = evens_gen(input_array)')
            # 6 function calls in 0.326 seconds
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.326    0.326 <string>:1(<module>)
   #      1    0.000    0.000    0.326    0.326 l_04_task_01.py:20(evens_gen)
   #      1    0.326    0.326    0.326    0.326 l_04_task_01.py:21(<listcomp>)
   #      1    0.000    0.000    0.326    0.326 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('output_array = evens_cyc(input_array)')
   #       502566 function calls in 0.610 seconds
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.011    0.011    0.610    0.610 <string>:1(<module>)
   #      1    0.502    0.502    0.599    0.599 l_04_task_01.py:27(evens_cyc)
   #      1    0.000    0.000    0.610    0.610 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   # 502561    0.097    0.000    0.097    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('output_array = evens_dic(input_array)')
   #       502565 function calls in 0.728 seconds
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.024    0.024    0.728    0.728 <string>:1(<module>)
   #      1    0.618    0.618    0.704    0.704 l_04_task_01.py:36(evens_dic)
   #      1    0.000    0.000    0.728    0.728 {built-in method builtins.exec}
   # 502561    0.086    0.000    0.086    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# ВЫВОДЫ:
# все алгоритмы №1, №2, №3 имеют линейную сложность O(n), т.к. время выполнения возрастает
# прямо пропорционально кол-ву элементов во входном массиве. Если принять время выполнения
# алгоритма №1 за единицу, то алгоритм №2 медленнее в 1,2 раза, алгоритм №3 - в 1.6 раз.
# Более высокое быстродействие алгоритма №1 обусловлено использованием генератора списка,
# вместо метода APPEND в алгоритмах №2, №3.