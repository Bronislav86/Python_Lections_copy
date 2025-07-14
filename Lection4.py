# ----------Мы можем присвоить значение функции какой-то переменной, то есть сделать так, чтобы переменная ссылалась
# на ту же область в памяти, что и функция и потом использовать функцию, вызывая её через имя переменной

# def f(x):
#     return x * x

# a = f
# print(a(5))
# print(f(5))

# --------Передача функции в функцию------------------------

# def calk1(a, b):
#     return a + b

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calk2, 5, 5)

# -------------Лямбда фунцкии---------------

# def calk2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))

# calk1 = lambda a,b: a + b
# #---------------Как это выгдядело до сокращения в лямбду!
# # def calk1(a, b):
# #     return a + b
# #--------------------------------------------
# math(calk1, 5, 45)

# ----Еще короче можно записать так:

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a,b: a + b, 5, 45)

# -----------Задача-----------------

# list = [1, 2, 3, 5, 8, 15, 23, 38]

# for num in list:
#     if num % 2 == 0:
#         print(f'[({num}, {num**2})', sep=", ", end="")

# Второй вариант решение - через кортеж

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)

# def select(f, col):
#     return [f(x) for x in col] # Эта ф-я возвращает список, в котором мы к каждому эл. применили функцию f

# def where (f, col):
#     return [x for x in col if f(x)] # Эта ф-я возвращает только те значения, которые прошли проверку f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 ==0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# -------------Функция MAP------------------

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

# data = "15 156 96 3 5 52 5"
# print(data)

# # data = data.split()
# # print(data)

# data = list(map(int, data. split()))
# print(data)

# def where (f, col):
#     return [x for x in col if f(x)] # Эта ф-я возвращает только те значения, которые прошли проверку f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 ==0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# ---------------Функция Фильтр!!!-----------

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 ==0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# ---------------Работа с файлами--------------

# colors = ['red', '79879', 'blue']
# data = open('file.txt', 'a', encoding='utf-8') #Здесь указываем режим в котором будем работать
# data.writelines(colors) #разделителей не будет
# data.close()

# with open('file.txt', 'w') as data: ## Режим записи
#     data.write('line 1\n')
#     data.write('line 3\n')

# print(56)

# path = 'file.txt'
# data = open('file.txt', 'r') # режим чтения
# for line in data:
#     print(line)
# data.close()
