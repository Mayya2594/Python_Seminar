# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def find_min(array):
    min_num = array[0]
    for i in range(len(array)):
        if min_num > array[i]:
            min_num = array[i]
    return min_num

def find_max(array):
    max_num = array[0]
    for i in range(len(array)):
        if max_num < array[i]:
            max_num = array[i]
    return max_num   

def replace_grade(array):
    min_grade = find_min(list_1)
    max_grade = find_max(list_1)
    for i in range(len(array)):
        if array[i] == max_grade:
            array[i] = min_grade
    return array

n = int(input("Введите количество оценок: "))
list_1 = []
for i in range(n):
    list_1.append(int(input("Введите оценку: ")))
print(list_1)
print(replace_grade(list_1))