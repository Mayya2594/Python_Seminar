# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random
n = int(input("Введите количество элементов массива 1: "))
list_1 = []
for i in range(n):
    list_1.append(random.randint(1, 100))
print(list_1)
m = int(input("Введите количество элементов массива 2: "))
list_2 = []
for i in range(m):
    list_2.append(random.randint(1, 100))
print(list_2)
result = set(list_1).intersection(set(list_2))
list_res = list(result)
list_res.sort()

# for i in range(len(list_res)):
#   for j in range(i + 1, len(kool)):
    #   if list_res[i] > list_res[i + 1]:
    #      temp = list_res[i]
    #      list_res[i] = list_res[i + 1]
    #      list_res[i + 1] = temp)

print(list_res)