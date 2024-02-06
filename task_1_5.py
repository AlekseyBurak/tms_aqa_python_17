import math
a = float(input("Введи a: "))
b = float(input("Введи b: "))
c = (math.sqrt(a ** 2 + b ** 2))
print("Длина гипотенузы:", round(c, 2))
s = a * b / 2
print("Площадь треугольника:", round(s, 2))