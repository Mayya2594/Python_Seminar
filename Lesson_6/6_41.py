# Задача 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном
# массиве выведет количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Сначала вводится число
# N — количество элементов в массиве  Далее записаны N чисел — элементы
# массива. Массив состоит из целых чисел. 

# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5			1 5 1 5 1

# Вывод:			Вывод:
# 0				2

n = int(input("Введите количество элементов в массиве: "))
list_1 = []
for i in range(n):
    list_1.append(int(input("Введите значение элемента массива: ")))
count = 0
for i in range(1, n - 1):
    if list_1[i] > list_1[i + 1] and list_1[i] > list_1[i - 1]:
        count += 1
print(count)