import math
print("Д/З № 3")
print("Task 1")
print("Заменить симво '#' на символ '/' в строке 'www.my_site.com#about'")
s = 'www.my_site.com#about'
print (f"преобразованная строка:  {s.replace("#", "/")}")
s = input("введите свою строку с символом #: ")
print (f"преобразованная ваша строка:  {s.replace("#", "/")}")

print("Task 2")
a = input("введите слово ")
print(f"слово + 'ing': {a + "ing"}")

print("Task 3")
s = input("введите строку с пробелами в начале и в конце: ")
print(f"первоначальная длина строки: {len(s)}")
print(f"преобразованная строка: {s.strip()}")
ss = s.strip()
print(f"конечная длина строки: {len(ss)}")

print("Task 4")
a = int(input("введите число в диапазоне от 0 до 255: "))
print(f"значению {a} соответствует символ {chr(a)}")

print("Task 5")
a = str(input("введите одиночный символ (только латиница): "))
print(f"{ord(a)} код символа {a} в таблице ASCII")

print("Task 6")
a = str(input("введите одиночный символ (только латиница): "))
print(f"код символа: {ord(a)}")
k = ord(a)
print(f"длина кода: {len(str(ord(a)))}")
l = len(str(ord(a)))
print("результат деления кв.корня кода на длину числа кода:")
print(math.sqrt(k) / l)
print(f"результат еще раз: {ord(a) ** 0.5 / len(str(ord(a)))}")

print("Task 6")
n = int(input("введите четырехзначное число: "))
print(f"единицы: {n % 10}")
print(f"десятки: {n % 100 // 10}")
print(f"сотни: {n % 1000 // 100}")
print(f"тысячи: {n % 10000 // 1000}")
