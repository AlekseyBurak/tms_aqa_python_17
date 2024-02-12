import math

a = int(input("\nВведи число от 0 до 255:"))
print("Символ в ASCII: " + str(chr(a)))

b = input("\nВведи символ латинского алфавита:")
print("Код в ASCII: " + str(ord(b)))

c = ord(b)
d = math.sqrt(c) / len(str(c))
print("Делить корень из ASCII на длину: " + str(d))
