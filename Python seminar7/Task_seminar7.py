
# def fun(x):
#     return x

# y = lambda x: x
# x = ['1', '2', '3']
# list_1 = list(map(int,x))
# print(list_1)

# st = "1 2 3"
# list_2 = st.split()
# print(list_2)
# # list_3 = list(map(int, list_2))
# # list_3 = list(map(int, st.split()))
# list_3 = list(map(int, input().split()))
# print(list_3)
# print(fun(5))
# print(y(5))
# print((lambda x: x) (5))

# Задача 47
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok
# trasformation = lambda x: x
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10

# def is_circle(tup):
#     if tup[0] == tup[1]:
#         return None
#     else:
#         return tup
# def find_squeare(tup):
#     x = 3.14 * tup[0] * tup[1]
#     return x
# def find_farthest_orbit(list_of_orbits):
#     true_orbits = list(map(is_circle, list_of_orbits))
#     list_of_squares = list(map(find_squeare, true_orbits))
#     return max(list_of_squares)

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(max(orbits, key= lambda x: x[0] * x[1] * (x[0] != x[1])))

