# Дополнить пятую задачу так чтобы выводился не просто код символа,
# а результат деления его квадратного корня на длину числа
# ( 100 ** 0,5 / 3 —- пример —- пускай 100 это код символа, тогда длинна числа три знака

a = input("Input letter\n")
b = ord(a)
c = len(str(b))
print((b ** 0.5) / c)