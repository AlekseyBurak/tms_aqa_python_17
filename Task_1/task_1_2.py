import math

a = int(input("Введи число x: "))
b = int(input("Введи число y: "))

print("|x| - |y|")
print("--------- =",
      (math.fabs(a) - math.fabs(b)) / (1 + math.fabs(a*b)))
print(" 1 + |xy|")
