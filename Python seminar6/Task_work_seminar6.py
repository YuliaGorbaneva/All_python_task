import random

# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод: 3 3 2 12
# (каждое число вводится с новой строки)


# print("Введите длину первого массива - ")
# a = int(input())
# print("Введите длину второго массива - ")
# b = int(input())
# list_1 = []
# list_2 = []

# for i in range(a):
#     list_1.append(random.randint(1,10))
# for j in range(b):
#     list_2.append(random.randint(1,10))
# print(list_1)
# print(list_2)

# for num in list_2:
#     # c = list_1.count(num)
    # while num in list_1: 
#     # if c > 0:
#         # for i in range(0, c):
#             list_1.remove(num)
# print(list_1)



# list_3 = []
# for i in range(len(list_1)):
#     for j in range(len(list_2)):
#         if list_1[i] != list_2[j]:
#             list_3.append(list_1[i])
#     print(list_3)



# Задача №41.
# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
# Ввод:
# 5
# 1 2 3 4 5 
# Вывод:
# 0
# Ввод:
# 5
# 1 5 1 5 1
# Вывод:
# 2
# (каждое число вводится с новой строки)

# print("Введите длину массива - ")
# n = int(input())
# list_1 = []
# for i in range(n):
#     list_1.append(random.randint(1, 10))
# print(list_1)
# b = 0
# for i in range(1, len(list_1) - 1):
#     # if list_1[i + 1] < list_1[i] > list_1[i - 1]:
#     if list_1[i + 1] < list_1[i] and list_1[i] > list_1[i - 1]:
#         b += 1
# print(b)


# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
# Ввод: 1 2 3 2 3
# Вывод: 2

print("введите длину списка - ")
n = int(input())
list_1 = []
c = 0
for i in range(n):
    list_1.append(random.randint(1,5))
print(list_1)
# list_2 = {}
# for i in list_1:
#     if i in list_2:
#         c += list_2[i]
#     list_2[i] = list_2.get(i, 0) + 1
# print(c)

list_2 = []
for i in list_1:
    for j in range(len(list_2)):
        if i == list_2[j]:
            c += 1
    list_2.append(i)
print(c)










# Задача №45.
# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10^5. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод: 
# 300
# Вывод:
# 220 284
# print("Введите число: ")
# n = int(input())
# def Summa(n):
#     c = 0
#     for i in range(1, n):
#         if n % i == 0:
#             c += i
#     return c
# # print(Summa(n))
# print("Введите диапозон поиска: ")
# k = int(input())
# list_1 = []
# for i in range(1, k + 1):
#     j = Summa(i)
#     if Summa(j) == i and i != j: 
#         list_1.append(j)
# print(list_1)