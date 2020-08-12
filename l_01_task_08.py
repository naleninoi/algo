# Урок 1, задача №8
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

# https://drive.google.com/file/d/1nB-ln98-G-3aJAJ5cLtOmatgqloYOoGT/view?usp=sharing

year = int(input('Введите целое число - год по григорианскому календарю: '))
if year % 4 == 0:
    if year % 100 != 0:
        print('Год високосный')
    elif year % 400 == 0:
        print('Год високосный')
    else:
        print('Год невисокосный')
else:
    print('Год невисокосный')
