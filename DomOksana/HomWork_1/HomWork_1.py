import math
print("Д/З № 1")
# задача 1
print("Task 1*")
print("введите два действительных числа ")
a = float(input("введите первое число a "))
b = float(input("введите второе число b "))
print(f"сумма чисел: {a + b}")
print(f"разность чисел: {a - b}")
print(f"произведение чисел: {a * b}")
# задача 2
print("Task 2*")
print("                    |x|-|y|")
print("дано выражение:    ---------")
print("                    1+ |xy|")
print("введите два действительных числа ")
x = float(input("введите число x "))
y = float(input("введите число y "))
print(f"значение выражения: {( (abs(x) - abs(y)) / (1 + abs(x * (y))))}")
# задача 3
print("Task 3")
print("дана длина ребра куба: 3 см")
a = 3
print(f"получен объем куба: {a ** 3} см3")
print(f"получена площадь боковой поверхности куба: {6 * a ** 2} см2")
# задача 4
print("Task 4*")
print("введите два натуральных числа ")
a = float(input("введите число a "))
b = float(input("введите число b "))
print(f"среднее арифметическое чисел: {((a + b) / 2)}")
print(f"среднее геометрическое чисел: {(math.sqrt(a * b))}")
# задача 5
print("Task 5*")
print("введите катеты прямоугольного треугольника")
a = int(input("введи катет a: "))
b = int(input("введи катет b: "))
print(f"гипотенуза треугольника: {math.sqrt(a ** 2 + b ** 2)}")
print(f"площадь треугольника: {( a * b / 2)}")