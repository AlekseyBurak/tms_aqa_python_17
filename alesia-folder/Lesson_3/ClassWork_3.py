print("hi everybody")

number_of_my_cats = 1  # good case
# umberOfMyCats = 1    - bad case
# Number = 1           - bad case
# print = 1            - bad case, зарезервированные имена
# "=" - это присваивание
a = "string"  # iterable
b = 'one more string'
c = """
this
is 
very
long
"""
d = '''
d
'''
print(a, b, c, d)
a = a[0] + 'T' + a[2:]
print(a)
a = "s" + "t"
print(a)

name = "alesia\n"
surname = "dirina"
print(name*3)
# print(name*surname) - bad case
e = r"C:\Users\Алеся\PycharmProjects\tms_aqa_python_17" # r - как строка, не путь
print(name.index("s"))

f = "jkhrdf kjshWefk ksjWk jlkj"
print(f.split())
print(f.split(sep="W"))
print(f.find("hrd"))

a1 = 9
b1 = 4
print(a1 / b1)
print(a1 // b1)
print(a1 % b1)
print(b1 % a1)

g = 0
g += 1  # g = g + 1

h = True
j = False
print(2 >= 8)

print("S" in "String")
print("s" in "String")
# print(1 in 111) - bad case, initerable!

k = "10"
print(int(k))
print(type(k))

print(bool(0))
print(bool(-1))  # все что не 0 - это True
print(bool("0"))  # строка с символами - True
print(bool(""))   # строка пустая - False

