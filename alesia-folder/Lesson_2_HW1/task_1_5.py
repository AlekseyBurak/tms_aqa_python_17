import math

a = int(input("Введи число - 1ый катет треугольника: "))
b = int(input("Введи число - 2ой катет треугольника: "))
print("Гипотенуза =", math.hypot(a, b),
      "\nПлощадь треугольника =", a*b/2)
