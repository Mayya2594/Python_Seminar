# list_1 = [1, 2, 3, -1.575, 'Hello', True]
# print(list_1[3])

# key: value
# list_2 = [5, 7]
# age = [{'Anna': 25, "Andrey": 33}, {"Ivan": 45, "Alexandr": 38}]
# print(age[1]['Ivan'])

# Задача 21. Напишите программу для печати всех уникальных
# значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]
values = set()

# Вариант 1:
# for i in data:
#     values.add(list(i.values())[0])
# print(values)

# Вариант 2:
for i in data:
    for key in i:
        values.add(i[key])
print(values)