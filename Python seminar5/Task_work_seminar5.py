# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где 
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# def Fib(n):
#     if n in [0]:
#         return 0
#     if n in[1,2]:
#         return 1
#     return Fib(n-1) + Fib(n-2)
# # list_1 = []
# n = int(input())
# # for i in range(n):
# #     list_1.append(Fib(i))
# # print(list_1)
# print(Fib(n))
    


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# print("введите количество оценок:")
# n = int(input())
# list_1 = []
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# max_num = max(list_1)
# min_num = min(list_1)
# for i in range(len(list_1)):
#     if list_1[i] == max_num:
#         list_1[i] = min_num
# print(list_1)




# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


# print("Введите число: ")
# n = int(input())
# def NaturNum(n, delim = 2):
#     # if delim == n:
#     if n == 2 or delim * delim > n:
#         return True
#     if n == 1:
#         return False
#     if n % delim == 0:
#         return False
#     return NaturNum(n, delim + 1)

# print(NaturNum(n))



# Задача №37. Решение в группах
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


# n = int(input())
# def NewRev(n):
#     if n == 0:
#         return
#     item = input()
#     NewRev(n-1)
#     print(item)
# NewRev(n)


# def Fin(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return Fin(n - 1) + f'{k}  '

# n = int(input())
# print (Fin(n))



# Факториал числа N

# num = int(input())
# def Factorial (num):
#     if num == 0:
#         return 1
#     if num == 1:
#         return num
#     return num * Factorial(num - 1)
# print(Factorial(num))



# Является ли строка полиндроммом
# n = []
# def Polindrom(n):
#     if len(n) < 2:
#         return True
#     elif n[0] != n[-1]:
#         return False
#     return Polindrom(n[1:-1])
# print(Polindrom("арозаупаланалапуазора"))

