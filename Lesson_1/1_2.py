a = int(input("Введите количество учащихся в 1 кабинете: "))
b = int(input("Введите количество учащихся во 2 кабинете: "))
c = int(input("Введите количество учащихся в 3 кабинете: "))
print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))

countStudents1 = int(input("Введите кол-во учеников в 1-ом кабинете: "))
countStudents2 = int(input("Введите кол-во учеников в 2-ом кабинете: "))
countStudents3 = int(input("Введите кол-во учеников в 3-ом кабинете: "))
part1 = (countStudents1 + 1) // 2
part2 = (countStudents2 + 1) // 2
part3 = (countStudents3 + 1) // 2
print(part1 + part2 + part3)