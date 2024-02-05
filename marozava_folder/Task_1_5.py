import math

c1 = int(input("Введите первый катет: "))
c2 = int(input("Введите второй число: "))
hypotenuse = math.sqrt(c1 ** 2 + c2 ** 2)
S = 0.5 * c1 * c2
print(f"Гипотенуза: {hypotenuse} \nПлощадь прямоугольного треугольника: {S}")
