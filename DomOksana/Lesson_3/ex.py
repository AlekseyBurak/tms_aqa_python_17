# a = input("введите глагол: ")
# print (a + "ing")
# f = "jkhrdf kjshWefk ksjWk jlkj"
# print(f.split())
# print(f.split(sep="W"))
# print(f.find("hrd"))
# a = "string"
# print(a[0])
# # не поменяет (только всю строку переписать sTring
# #a[2] = 'T'
# print(a)
# a = a[0] + 'T' + a[2:]
# print(a)

# примеры использования методов для срок
#string = "          Я длинная строка с разными недостатками и скрытыми секретами           "



#print(s.replace("#", "/"))
# f = "jkhrdf kjshWefk ksjWk jlkj"
# print(f.split())
# print(f.split(sep="W"))
# p = input(s.find("#"))
# print(p)
# print("000")
# r = int(p)
# print(r)
# a = a[r] + '/' + a[(r + 2):]
# print(a)
#print(s.replace("#", "/"))

# s = input("введите строку: ")
# print (f"преобразованная строка:  {s.replace("#", "/")}")
s = input("введите строку с пробелами в начале и в конце: ")
print(f"первоначальная длина строки: {len(s)}")
print(f"преобразованная строка: {s.strip()}")
ss = s.strip()
print(f"конечная длина строки: {len(ss)}")