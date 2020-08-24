# Урок 4, задача №2

# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».

import math, timeit, cProfile


# АЛГОРИТМ №1 — с использованием «Решета Эратосфена».
def sieve(n):
    # вложенная функция для нахождения верхней границы интервала, в к-ром находится i-е простое число
    def upper_bound(prime_index):
        num_of_primes = 0
        upper_bound = 2
        while num_of_primes <= prime_index:
            num_of_primes = upper_bound / math.log(upper_bound)
            upper_bound += 1
        return upper_bound

    max_num = upper_bound(n)
    spam = [i for i in range(max_num)]
    spam[1] = 0

    for i in range(2, max_num):
        if spam[i] != 0:
            j = i * 2
            while j < max_num:
                spam[j] = 0
                j += i

    result = [i for i in spam if i != 0]
    return result[n - 1]


# АЛГОРИТМ №2 — без использования «Решета Эратосфена».
def prime(n):
    if n == 1:
        return 2
    else:
        prime_numbers = [2]
        num = 1
        while len(prime_numbers) < n:
            num += 2
            for i in prime_numbers:
                if num % i == 0:
                    break
            else:
                prime_numbers.append(num)
        return num


# при N = 10
# 0.003234736000000002
# 0.0011780519999999989

# при N = 50
# 0.027066508999999996
# 0.012723343000000012

# при N = 100
# 0.051405752
# 0.04008625499999999

# при N = 250
# 0.164111765
# 0.24044541000000003

# при N = 500
# 0.332105062
# 0.967414768

# при N = 1000
# 0.759820407
# 3.863373104

# при N = 2000
# 1.66382386
# 15.44513504

print(timeit.timeit('sieve(2000)', number=100, globals=globals()))
print(timeit.timeit('prime(2000)', number=100, globals=globals()))

# при N = 10000
cProfile.run('sieve(10000)')
   #       116678 function calls in 0.330 seconds
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.002    0.002    0.330    0.330 <string>:1(<module>)
   #      1    0.126    0.126    0.328    0.328 l_04_task_02.py:15(sieve)
   #      1    0.121    0.121    0.173    0.173 l_04_task_02.py:17(upper_bound)
   #      1    0.016    0.016    0.016    0.016 l_04_task_02.py:26(<listcomp>)
   #      1    0.013    0.013    0.013    0.013 l_04_task_02.py:36(<listcomp>)
   #      1    0.000    0.000    0.330    0.330 {built-in method builtins.exec}
   # 116671    0.052    0.000    0.052    0.000 {built-in method math.log}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(10000)')
   #       62368 function calls in 11.050 seconds
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000   11.050   11.050 <string>:1(<module>)
   #      1   11.034   11.034   11.050   11.050 l_04_task_02.py:41(prime)
   #      1    0.000    0.000   11.050   11.050 {built-in method builtins.exec}
   #  52365    0.014    0.000    0.014    0.000 {built-in method builtins.len}
   #   9999    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ВЫВОДЫ:
# При малых значениях N алгоритм №2 (без "решета") имеет некоторое преимущество.
# Однако при N>200 становится очевидно, что алгоритм №1 ("решето") гораздо более эффективен.
# Слабое место алгоритма №2 - перебор делителей в постоянно пополняющемся списке
# простых чисел.
# Исходя из составленных графиков, можно предположить, что алгоритм №1
# имеет линейную сложность O(n), тогда как алгоритм №2 имеет сложность O(n**2 - n).

# График
# https://drive.google.com/file/d/1KAVukIzz8sZbEpy7vBTiKQ3qSjUibSf4/view?usp=sharing