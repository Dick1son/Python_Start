# Task 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# from decimal import Decimal

# def SumDigits (num):
#     flot = False
#     counter = 0
#     for i in num:
#         if i == "." or i == ",":
#             flot = True
#             break
#         counter += 1
#     match flot:
#         case False:
#             number = int(num)       
#             sum = 0
#             while number > 0:
#                 sum += number % 10
#                 number //= 10
#             return sum
#         case True:
#             number = Decimal(num)
#             for i in range(counter):
#                 number /= Decimal("0.1")
#             sum = 0
#             while number > 0:
#                 sum += number % 10
#                 number //= 10
#             return sum

# num = input("Введите число: ")

# print(f'Сумма чисел равна {SumDigits(num)}')

# Task 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# def Myltiply(num):
#     res = 1
#     for i in range(1,num + 1):
#         res *= i
#         print(res)

# num = int(input("Введите число: "))
# Myltiply(num)

# Task 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой. COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.
def CrossLines (line1 , line2):
    counter = 0
    for i in range(len(line1)): 
        if line1[i:i + len(line2)] == line2: counter += 1
    return counter

line1 = input("Введите строку, в которой будем искать: ")
line2 = input("Введите строку, которую будем искать: ")

print(CrossLines(line1, line2))
