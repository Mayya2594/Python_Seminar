# Задача 49. Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка
# орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж
# из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле
# S = pi*a*b, где a и b - длины полуосей эллипса. При решении задачи используйте
# списочные выражения. Подсказка: проще всего будет найти эллипс в два шага:
# сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна.

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# ВАРИАНТ 1:
# def find_farthest_orbit(list_of_orbits):
#     index = 0
#     S_max = 0
#     for i in range(len(list_of_orbits)):
#         if list_of_orbits[i][0] == list_of_orbits[i][1]:
#             i +=1
#         S = list_of_orbits[i][0] * list_of_orbits[i][1]
#         if S > S_max:
#             S_max = S
#             index = i
#     return list_of_orbits[index]

# ВАРИАНТ 2:
def find_farthest_orbit(list_of_orbits):
    list_of_elept_orbits = [i for i in orbits if i[0] != i[1]]
    list_of_areas = [i[0] * i[1] for i in list_of_elept_orbits]
    # max_area_index = list_of_areas.index(max(list_of_areas))
    max_area_index = [i for i in range(len(list_of_areas)) if list_of_areas[i] == max(list_of_areas)]
    return list_of_elept_orbits[max_area_index[0]]

print(*find_farthest_orbit(orbits))