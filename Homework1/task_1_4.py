import math
print("Домашка 1. Задача 4- нахождение среднего арифметического и среднего геометрического двух действительных чисел")
print("Введите первое число")
x = float(input())
print("Введите второе число")
y = float(input())
a = (x + y)/2
g = math.sqrt(x * y)
print(f"Среднее ариметическое {a}\nСреднее геометрическое {g}")
