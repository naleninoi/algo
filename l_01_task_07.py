# По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

# https://drive.google.com/file/d/1nB-ln98-G-3aJAJ5cLtOmatgqloYOoGT/view?usp=sharing

a = float(input('Введите длину первого отрезка: '))
b = float(input('Введите длину второго отрезка: '))
c = float(input('Введите длину третьего отрезка: '))
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('Такой треугольник не существует')
else:
    if a != b and a != c and b != c:
        print('Это разносторонний треугольник')
    elif a == b and b == c:
        print('Это равносторонний треугольник')
    else:
        print('Это равнобедренный треугольник')
