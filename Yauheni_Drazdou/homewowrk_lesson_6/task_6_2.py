def fun():
    while True:
        print("Введите операцию:\n1-Сложение  "
              "2-Вычитание  3-Умножение  4-Деление  5-Выход")
        move = int(input())

        if move == 5:
            break

        #try:
            #move != int
        #except ValueError:
            #print("kf")

        if move > 5 or move < 1:
            print("Число должно быть от 1 до 5\nВведите операцию:\n"
                  "1-Сложение  2-Вычитание  3-Умножение"
                  "  4-Деление  5-Выход")
            continue
        print("Введите первое число")
        a = int(input())
        print("Введите второе число")
        b = int(input())

        if move == 1:
            print(f"Сумма {a + b}")
            try:
                c = (a + b) / 0
            except ZeroDivisionError:
                c = "На ноль делить нельзя"
            print(c)

        if move == 2:
            print(f"Разность {a - b}")
            try:
                c = (a - b) / 0
            except ZeroDivisionError:
                c = "На ноль делить нельзя"
            print(c)

        if move == 3:
            print(f"Произведение {a * b}")
            try:
                c = (a * b) / 0
            except ZeroDivisionError:
                c = "На ноль делить нельзя"
            print(c)

        if move == 4:
            print(f"Частное {a / b}")
            try:
                c = (a / b) / 0
            except ZeroDivisionError:
                c = "На ноль делить нельзя"
            print(c)


print(fun())





