# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

S = int(input("Введите значение суммы двух чисел: "))
P = int(input("Введите значение произведения двух чисел: "))
D = S * S - 4 * P
from math import sqrt
num1 = int((S - sqrt (D)) / 2)
num2 = int((S + sqrt (D)) / 2)
print(f'{S}, {P} -> {num1}, {num2}')

# x = int(input("Введите значение суммы двух чисел: "))
# y = int(input("Введите значение произведения двух чисел: "))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)