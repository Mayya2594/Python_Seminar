# Задача 43. Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные друг другу
# образуют одну пару, которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных строках.
# Ввод:       Вывод:
# 1 2 3 2 3   2

list1 = [int(i) for i in input("Введите числа: ").split()]
result = {}
for i in list1:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(sum([i // 2 for i in result.values()]))