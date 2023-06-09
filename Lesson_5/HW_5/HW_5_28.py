# Задача 28: Вводится десятичное число. Реализовать алгоритм его
# перевода в двоичную систему счисления через рекурсию.
# Нельзя использовать функцию bin()

# *Пример:*
#     10
#     *Вывод:*
#     1010

def binary(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    return binary(num // 2) + str(num % 2)

n = int(input("Введите число: "))
print(binary(n))