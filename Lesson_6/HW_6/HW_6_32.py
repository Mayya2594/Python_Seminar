# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

#         0  1  2  3   4   5  6  7   8   9 10 11  12 13  14  15 16  17  18 19
list1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_num = int(input("Введите минимальное значение: "))
max_num = int(input("Введите максимальное значение: "))
index = []
for i in range(len(list1)):
    if min_num <= list1[i] <= max_num:
        index.append(i)
print(*index)