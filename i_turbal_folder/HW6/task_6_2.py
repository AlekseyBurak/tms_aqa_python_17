def my_calculater() -> int:
    print("""
    Выберите операцию:
    1. Сложнение
    2. Вычитание
    3. Умножение
    4. Деление 
    5. Возведение в степень
    6. Корень из числа 
    7. Выход
    """)
    oper = ""
    while oper != "7":
        oper = input("Выберите операцию ")
        if oper == "7":
            break
        elif oper not in "1234567":
            print("Ошибка, запустите программу заново")
            break
        x = int(input("Введите первое число "))
        y = int(input("Введите второе число "))

        if oper == "1":
            print(x + y)

        elif oper == "2":
            print (x - y)
        elif oper == "3":
            print(x*y)
        elif oper == "4":
            if y == 0:
                print("Делить на нуль нельзя")
            else:
                print(x/y)
        elif oper == "5":
            print(x ** y)
        elif oper == "6":
            print(x ** (1/y))

my_calculater()



