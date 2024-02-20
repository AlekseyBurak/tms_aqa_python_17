def fun(*args):
    while True:
        print("Введите операцию:\n1-Сложение  2-Вычитание  3-Умножение  4-Деление  5-Выход")
        move = int(input())
        if move == 5:
            break
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        if move == 1:
            print(f"Сумма {a + b}")

        if move == 2:
            print(f"Разность {a - b}")

        if move == 3:
            print(f"Произведение {a * b}")

        if move == 4:
            print(f"Частное {a / b}")


print(fun())



