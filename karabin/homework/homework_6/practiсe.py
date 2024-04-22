# определение функции
# def sayHello():
#     print('Hello')
#     print('world')
#     print('anf anybody')
#
#
# sayHello()
# print('pause')
# sayHello()

# def square(x):
#      print('Квадрат числа ',x, '=' ,x**2)
# # square(5)

# def square(x):
#      print('Квадрат числа ',x, '=' ,x**2)
#
# for i in range(1,11):
#     square(i) # нельзя вводить два значения

# def multiply(a,b):
#     print(a*b)
#
# multiply(3,4)

# def even(a):
#     if a%2==0:
#         print(a, 'Четное')
#     else:
#         print(a, 'Нечетное')
#
# for i in range(20,31):
#     even(i)

# def factorial(n):
#     pr = 1
#     for i in range(2, n+1):
#         pr = pr*i
#     print(pr)
#
# factorial(6)

# import turtle
#
# def move():
#     turtle.forward(100)
#     turtle.left(90)
# def drawSquare():
#     for i in range(4):
#         move()
#
# turtle.speed(1)
#
# drawSquare()
# turtle.goto(150,150)
# drawSquare()

# import turtle
# def move(a):
#     turtle.forward(a)
#     turtle.left(90)
# def drawSquare(a):
#     for i in range(4):
#         move(a)
#
# turtle.speed(1)
#
# drawSquare(60)
# turtle.goto(150,150)
# drawSquare(120)

# не возвращает значение
# def square (x):
#     print(x**2)
#
# a = square(6)
# print(a)

# возвращает значение
# def square (x) :
#     return x**2
#
# a = square(square(3))
# print(a)

# def example():
#     print(1)
#     print(2)
#     return 'hello' #после return происходит выход из функции
#     print(3)
#     print(4)
#
# example()

# # не оптимальный вариант
# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False
#
# for i in range(1,11):
#     print(i, even(i))

# оптимальный вариант
# def even(x):
#     return x%2==0
#
# for i in range(1,11):
#     print(i, even(i))

# возвращает Tuple
# def sq_and_per(a, b):
#     return a * b, 2* (a + b)
#
# print(sq_and_per(3, 6))

# def sq_and_per(a, b):
#     return a * b, 2* (a + b)
#
# square, perimetr = sq_and_per(2, 5)
# print(square, perimetr)


# def buckets():
#     flb = 0
#     tlb = 0
#     print(f"{tlb=}, {flb=}")
#     while flb !=4:
#         choice = (input("Make your choice:\n"
#                         "1. Pour water into a 5 liter bucket \n"
#                         "2. Pour water into a 3 liter bucket \n"
#                         "3. Pour out water from a 5 liter bucket \n"
#                         "4. Pour out water from a 3 liter bucket \n"
#                         "5. Pour over from 5 liter bucket into 3 liter bucket \n"
#                         "6. Pour over from 3 liter bucket into 5 liter bucket \n"
#                         "Make your choice: "))
#
#         if choice == "1":
#             return flb == 5
#         elif choice == "2":
#             return tlb == 3
#         elif choice == "3":
#             return flb == 0
#         elif choice == "4":
#             return tlb == 0
#         elif choice == "5":
#             # if
#             #     return flb == flb - tlb
# # flb = 0
# # tlb = 0
# # print(f"{tlb=}, {flb=}")
# buckets()
# Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
# num1, num2, num3 = int(input()), int(input()), int(input())
#
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
#
# print(counter)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if -1 <= (a - c) <= 1 and -1 <= (b - d) <= 1:
    print("YES")
else:
    print("NO")
