import random


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# print("Введите длину первого массива: ")
# n = int(input())
# print("Введите длину второго массива: ")
# m = int(input())

# mass_1 = []
# mass_2 = []
# print("Введите элементы первого массива:")
# for i in range(n):
#     mass_1.append(int(input()))
#     # mass_1.append(random.randint(1, 20))
# for j in range(m):
#     mass_2.append(random.randint(1, 20))

# print(mass_1)
# print(mass_2)
# mass_1.sort()
# mass_2.sort()

# mass_3 = list(set(mass_1 + mass_2))

# print(mass_3)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

print("Введите число грядок: ")
gr = int(input())
berry = []
maximum = 0
for i in range(gr):
    berry.append(random.randint(100, 10000))
print(berry)
for j in range(len(berry)):
    if len(berry[j: j+3]) < 3:
        berry.append(berry[0])
        berry.append(berry[1])
    summa = sum(berry[j: j+3])
    print(f"{j}-{berry[j: j+3]} = {summa}")
    if maximum < summa:
        maximum = summa

print(f"максимальное количество ягод {maximum}")



