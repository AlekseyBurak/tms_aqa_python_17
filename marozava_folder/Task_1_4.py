import math

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
Arithmetic_Mean = (x + y) / 2
Geometric_Mean = math.sqrt(x * y)
print(f"Среднее арифметическое: {Arithmetic_Mean} \nСреднее геометрическое: {Geometric_Mean}")