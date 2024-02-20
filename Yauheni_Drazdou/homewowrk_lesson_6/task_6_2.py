def fun(*args):
    print("Введите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Выход")
    move = int(input())

    while move < 5:
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        if move == 1:
            print("Сумма")
            return a + b
        if move == 2:
            print("Разность")
            return a - b
        if move == 3:
            print("Произведение")
            return a * b
        if move == 4:
            print("Частное")
            return a / b

print(fun())
