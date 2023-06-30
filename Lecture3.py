# Функции, рукерсия, алгоритмы
# Функция - это фрагмент программы, импользуемый многократно

# def function_name(x) - склько аргументов передаем, столько и принимаем

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa
#     # print(summa)
# a = sumNumbers(5)
# print(a)


# def summStr(*args):  #(* ) - не ограниченное количество аргументов
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(summStr('q', 'e', 'l'))
# print(summStr('df','f','ert','er'))

#Модульность
# import Modul1
# print(Modul1.max1(5, 9))

# from Modul1 import max1
# print(max1(10,9))

# from Modul1 import *
# print(max1(10,9))

# import Modul1
# print(Modul1.max1(11, 12))

# import Modul1 as m1      # as - переиминовывает функция в программе на время работы с ней
# print(m1.max1(10,8))

# Рекурсия - это функция , вызывающаяя сама себя.
# При описании рекурсии важно указать, когда функции надо остановиться и перестать вызывать саму себя.
# ПО-другому говоря , необходимо указать базис рекурсии

# def  Fib(n):
#     if n in [1, 2]:
#         return 1
#     return Fib(n-1) + Fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(Fib(i))
# print(list_1)


# Алгоритмы - набор инструкций для выполнения некоторой задачи
# 2 самых интересных алгоритма сортировки
#   1. Быстрая сортировка
#   2. Сортировка слияниянием


#Быстрая сортировка
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([14,4,4,78,4,8,4,6,7,6,5]))
print(quick_sort([10,2,5]))

# Сортировка слиянием
def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left= nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list_1 = [1,2,2,5,4,6,5,7,4,6,5,5,9,5,6,]
mergeSort(list_1)
print(list_1)