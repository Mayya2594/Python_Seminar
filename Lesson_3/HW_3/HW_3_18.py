# Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов массива: "))
list_1 = []
for i in range(n):
    list_1.append(int(input("Введите значение элемента массива: ")))
x = int(input("Введите число: "))
list_diff = []
for i in range(n):
    list_diff.append(abs(x - list_1[i]))
index = 0
min_delta = list_diff[index]
for i in range(n):
    if list_diff[i] < min_delta:
        min_delta = list_diff[i]
        index = i
print(list_1[index])