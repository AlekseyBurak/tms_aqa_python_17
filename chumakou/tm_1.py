# a = input("Введи имя \n")
# print("Привет", a)

import math



print("------ Number 1 ------")
a = 2
b = 2
sum = a + b
minus = a - b
multiply = a * b
print("+", sum)
print("-", minus)
print("*", multiply)





print("------ Number 2 ------")

print(int(abs(2) - abs(5) / 1 + 2 * 5)) #Задание в одну строчку







print("------ Number 3 ------")

def найти_объем_и_площади(a):
    объем = a**3
    площадь_полная = 6 * a**2
    площадь_боковая = 4 * a**2
    return объем, площадь_полная, площадь_боковая

a = 3

объем, площадь_полная, площадь_боковая = найти_объем_и_площади(a)


print(f"Объем куба: {объем}")
print(f"Площадь полной поверхности: {площадь_полная}")
print(f"Площадь боковой поверхности: {площадь_боковая}")




print("------ Number 4 ------")

number1 = float(input("Введи первое число: "))
number2 = float(input("Введи второе число: "))

avg_ari = (number1 + number2) / 2
avg_geo = (number1 * number2) ** 0.5

print("Среднее арифметическое:", avg_ari)
print("Среднее геометрическое:", avg_geo)






print("------ Number 5 ------")

def find_g_i_p(cat_1, cat_2):
    gipotenuza = math.sqrt(cat_1**2 + cat_2**2)
    ploshad = 0.5 * cat_1 * cat_2
    return gipotenuza, ploshad

cat_1 = 2
cat_2 = 2

print(f"Гипотенуза: {find_g_i_p(cat_1, cat_2)[0]}")
print(f"Площадь: {find_g_i_p(cat_1, cat_2)[1]}")