# task_1
a = float(input("введите число a: "))
b = float(input("введите число b: "))
print("сумма a и b равна", a + b,
      "\nразность a и b равна ", a - b,
      "\nпроизведение a и b равно ", a * b)

# task_2
x = float(input("введите число x: "))
y = float(input("введите число y: "))
print((abs(x) - abs(y)) / (1 + abs(x * y)))

# task_3
a = int(input("введите длину ребра куба: "))
print(f"объем куба V = {a ** 3} \nплощадь боковой поверхности куба S = {4 * a ** 2 }")

# if a <= 0:
#     print("длина ребра не может быть отрицательной или равной 0")
# else:
#     print("объем куба V =", a ** 3,
#           "\nплощадь боковой поверхности куба S =", 6 * a ** 2)

# task_4
import math
a = float(input("введите число a: "))
b = float(input("введите число b: "))
print(f"среднее арифметическое = {(a + b)/2} \nсреднее геометрическое = {math.pow(a * b, 1/2)}")

# task_5
import math
x = int(input("введите длину первого катета: "))
y = int(input("введите длину второго катета: "))
print(f"длина гипотенузы равна {math.sqrt(x**2 + y**2)} \nплощадь треугольника равна {(x * y)/2}")