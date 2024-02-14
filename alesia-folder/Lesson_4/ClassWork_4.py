# git pull origin main
import math
from random import random

l = [1, 9327649, "text", 0.9, None, True, False, [1, 2]]
l1 = list("text")

print(l)
print(l1)
print(l[-8])
print(l[1:3])
print(l[-4:-1])
print(l[::-1])  # inversion
print(l[0::2])  # все с шагом 2

l2 = "04.03.2020 - text with a lot of smth"
print(l2[13::1])  # срез с 13-го символа и до конца

l3 = [1, 2, 3]
l3.reverse()
print(l3)
# l3.copy

# l4 = [3, 2, 1, 5, 8]
#print(l4.sort())

# def my_func(e)

a = [1, 2, 3]
c = a
b = [1, 2, 3]
print(a == b)  # ок по равенству
print(a is b)  # не ок по равенству элементов
print(a is c)  # ок по равенству элементов

l6 = [1, 2, 3]
l6.append(4)
l6.append("text")
print(l6)
l6.insert(5, 5)
print(l6)

l7 = [1, 2, 3, 3, 4, 5]
l7.remove(3)  # первый встречающийся
print(l7)
l7.pop(1)
print(l7)
l8 = [1, 2, 3, 3, 4]
print(l8.count(3))  # ???

# clear
# remove

t = ()  # кортеж, неизменяемый
t = tuple()

print(type(()))
print(type((1, )))

text = "text"
l_text = list(text)
t_text = tuple(text)
print(t_text)
print(l_text)
print(t_text[0:2])

# распаковка
l_unpack = [1, 2, 3, 4, 5, 6, 7, 8]
a, b, c, *rest = l_unpack
print(a)
print(b)
print(c)
print(rest)

text1 = "this is long string"
splited = text1.split()
# TODO splited[0], splited[1], splited[2]

s = {1, 2}
# s = set()
# set_1 = {1, 2, 3, [4, 5]}  # bad case
set_2 = {1, 2, 3, (4, 5), 1, 2}
print(set_2)

s1 = set("Эй, жлоб! Где туз? Прячь юных съёмщиц в шкаф.")  # панграмма
print(s1)

s2 = {1, 2, 3, 4, 5}  # у элементов сета нет индексов
s2.add(6)
print(s2)
s2.remove(6)
print(s2)

print(s2.pop())  # удаляет любой элемент
# clear, revert

fr_set = frozenset(s)
print(type(fr_set))

ord_set_zero = {0, 1, 2, True, False}
ord_set_no_zero = {1, 2, True, False}
print(ord_set_zero)
print(ord_set_no_zero)

# Словари = хэш-таблицы
d = {}  # пустой словарь
dict1 = {
    "apple": 10,
    "banana": 8,
    "pear": 12
}
dict2 = {
    "appl": 10,
    8: 8
}
print(dict1["apple"])
dict1["cucumber"] = 9
print(dict1)
dict1["apple"] = 11
print(dict1)
dict1["apple"] = {"redprince": 7, "antonovja": 6}
print(dict1)

# is, is not
# in, not in

print("apple" in dict1)
print(11 in dict1)

print(dict1.items())
print(dict1.keys())
print(dict1.get("apple"))

# IF
# num = random.randint(1, 10)
num = 5
print(num)
if num > 5:
    print("не больше 5")
elif num < 5:
    print("меньше 5")
else:
    print("равно 5")

t1 = "text"
if "xt" in t1:
    print("Da")
# if "xt" ==

# FOR

lis = [i for i in range(10)]

for item in lis:
    print(item)
print("stop")

lis2 = ["text", "wrong text", "no text"]

for item in lis2:
    if item == "wrong text":
        print("wrong text found")

for letter in lis2:
    print(letter, end='_')

for key, value in dict1.items():
    print(f"{key=} -- {value=}")

for key, value in dict1.items():
    if value == 8:
        print(f"{key} -- {value}")

for i in range(4):
    print("I'm for")

num1 = random.randint(1, 5)
while num1 !=2:
    print(num1)
    print("No not eq to 2")
    num1 = random.randint(1, 5)
print()
print(num1)

num2 = 0
while num2 < 8:
    print(f"{num2}, less then 8")
    num2 += 1