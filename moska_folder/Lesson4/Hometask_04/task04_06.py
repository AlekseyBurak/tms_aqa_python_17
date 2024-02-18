# не поняла, как сделать исключение подсчета знаков припенания и специальных символов
string = "shine bright like a diamond"
slovar = {}
for char in string:
    if char in slovar:
        slovar[char] += 1
    else:
        slovar[char] = 1

popular_bukva = max(slovar, key=slovar.get)
print(popular_bukva)
a = input()
b = input()
c = input()
print(c, b, a, sep="\n")
