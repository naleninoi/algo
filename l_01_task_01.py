# Урок 1, задача №1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# https://drive.google.com/file/d/1nB-ln98-G-3aJAJ5cLtOmatgqloYOoGT/view?usp=sharing


a = int(input('Введите целое трехзначное число: '))
h = a // 100
d = (a // 10) % 10
u = a % 10
res_sum = h + d + u
res_mult = h * d * u
print (h, d, u)
print (f'Сумма цифр числа составляет {res_sum}, произведение цифр составляет {res_mult}.')
