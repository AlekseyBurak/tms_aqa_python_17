x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
result = (abs(x) - abs(y)) / (1 + abs(x * y))
print("Результат:", result)