x = float(input("Введи x: "))
y = float(input("Введи y: "))
z = (abs(x) - abs(y)) / (1 + (abs(x) * abs(y)))
print("Итог вычислений:", round(z, 4))
