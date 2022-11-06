# Task 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# def SimplyMultipliers(num):
#     list = []
#     counter = 2
#     while num != 1:
#         if num % counter == 0:
#             list.append(counter)
#             num //= counter
#         else:
#             counter += 1
    
#     return list

# def UserInput():
#     while True:
#         try:
#             return int(input("Введите натуральное число: "))
#         except ValueError:
#             print("Try again.")

# print(SimplyMultipliers(UserInput()))

# Task 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# def DelRepeat(list):
#     list1 = []
#     for i in list:
#         if i not in list1: list1.append(i)
#     return list1

# def UserInput():
#     list = []
#     sheet = input("Введите последовательность чисел через пробел: ")
#     for i in sheet:
#         if i == " ": continue
#         else:
#             try:
#                 int(i)
#             except ValueError:
#                 print("Обнаружена ошибка ввода.")
#         list.append(int(i))
#     return list

# print(DelRepeat(UserInput()))

# Task 3.  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random

def write_file(st):
    with open('HW_3.txt', 'a') as data:
        data.write(st)
        data.write("\n")

def create_mn(k):
    lst = [random.randint(0,101) for i in range(k+1)]
    return lst
    
def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

def UserInput():
    while True:
        try:
            return int(input("Введите натуральную степень k = "))
        except ValueError:
            print("Try again.")

write_file(create_str(create_mn(UserInput())))