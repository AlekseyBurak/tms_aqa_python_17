#1
a = 'www.my_site.com#about'
print (a.replace('#', '/'))

#2
a = input()
print(a + 'ing')

#3
a = input()
print(a.strip())

#4
a = int(input("Введите число от 0 до 255:\n"))
print(chr(a))

#5
a = input('Введите одиночный символ латиницей:\n')
print(ord(a))

#6
a = input('Введите одиночный символ латиницей:\n')
print(ord(a) ** 0.5 / len(str(ord(a))))

#7
a = int(input('Введите четырёхзначное число:\n'))
print("Единицы:", a % 10, "Десятки:", (a % 100) // 10, "Сотни:", (a // 100) % 10, "Тысячи:", a // 1000, sep='\n')
