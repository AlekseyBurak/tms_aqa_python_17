def fun2():
    user_choice = input(f"Выберите операцию?\n"
                        f"сложение - press 1\n"
                        f"вычитание - press 2\n"
                        f"умножение - press 3\n"
                        f"деление - press 4\n"
                        f"выход - press 5\n"
                        )
    if user_choice == "5":
        return
    else:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

    if user_choice == "1":
        print(a + b)
    elif user_choice == "2":
        print(a - b)
    elif user_choice == "3":
        print(a * b)
    elif user_choice == "4":
        if b == 0:
            print("Учи матчасть. На ноль делить нельзя")
            b = int(input("Введите второе число, отличное от нуля: "))
            print(a / b)
        else:
            print(a / b)
    fun2()


fun2()
