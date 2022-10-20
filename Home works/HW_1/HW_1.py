# Task 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# def CheckDay(day):
#     if day == 6 or day == 7:
#         weekend = True
#         print(f"{day} -> да")
#     elif day > 0 and day < 8:
#         weekend = False
#         print(f"{day} -> нет")
#     else:
#         print("Введено не корректное число")

# while(1):
#     try:
#         day = int(input("\nВведите день недели как число: "))
#     except ValueError:
#         print("Введено не корректное число")
#         exit(0)

#     CheckDay(day)
    
# Task 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# for x in range(2):
#         for y in range(2):
#             for z in range(2):
#                 print(f"{x} {y} {z} -> {not (x or y or z) == (not x and not y and not z)}\n")

# Task 3.  Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
def CheckQuadrant(x, y):
    if x == 0 or y == 0:
        print("Точка находится на осях")
    elif x > 0 and y > 0:
        print("Точка находится в первой четверти")
    elif x < 0 and y > 0:
        print("Точка находится во второй четверти")
    elif x < 0 and y < 0:
        print("Точка находится в третей четверти")
    elif x > 0 and y < 0:
        print("Точка находится в четвертой четверти")
    else:
        print("Некорректные координаты")

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))

CheckQuadrant(x ,y)

