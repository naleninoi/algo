# Урок 5, задача №1

# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль
# выше среднего и ниже среднего.

from collections import defaultdict

revenue = defaultdict(list)
firms_low = defaultdict(list)
firms_high = defaultdict(list)
total_rev = 0

# ввод кол-ва предприятий, названия предприятий, прибыли по каждому из 4 кварталов
firms = int(input('Введите количество предприятий для анализа прибыли: '))
for n in range(1, firms + 1):
    firm_name = input(f'Введите название предприятия №{n}: ')
    for q in range(1, 5):
        quart_rev = float(input(f'Введите прибыль для предприятия "{firm_name}" в квартале {q}: '))
        revenue[firm_name].append(quart_rev)

# вычисление общей годовой и средней годовой прибыли по всем предприятиям
for val in revenue.values():
    total_rev += sum(val)
ann_rev = total_rev / firms

# вычисление общей годовой прибыли по каждому предприятию, сортировка по размеру прибыли
for key, val in revenue.items():
    firm_rev = sum(val)
    if firm_rev < ann_rev:
        firms_low[key].append(firm_rev)
    else:
        firms_high[key].append(firm_rev)

# вывод результатов
print(f'Средняя годовая прибыль по всем {firms} предприятиям составила {ann_rev:.2f} руб.')
print('Предприятия с годовой прибылью ниже средней: ')
for key, val in firms_low.items():
    print(f'"{key}" - {val[0]} руб.')
print('Предприятия с годовой прибылью выше или равной средней: ')
for key, val in firms_high.items():
    print(f'"{key}" - {val[0]} руб.')
