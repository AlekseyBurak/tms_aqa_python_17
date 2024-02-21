# # task1
# def fun1(some_string: str) -> str:
#     some_string = input("input some string: ").lower() + " "
#     new_string = ""
#     count = 1
#     for ind in range(1, len(some_string)):
#         if some_string[ind - 1] == some_string[ind]:
#             count += 1
#         else:
#             new_string += some_string[ind - 1] + str(count)
#             count = 1
#     print(new_string)
#     return new_string
#
#
# fun1("")

# task2


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

    first_number = int(input("Введите первое число: "))
    second_number = int(input("Введите второе число: "))

    while user_choice != "5":
        if user_choice == "1":
            print(first_number + second_number)
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
                first_number = int(input("Введите первое число: "))
                second_number = int(input("Введите второе число: "))

        elif user_choice == "2":
            print(first_number - second_number)
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
                first_number = int(input("Введите первое число: "))
                second_number = int(input("Введите второе число: "))

        elif user_choice == "3":
            print((first_number * second_number))
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
                first_number = int(input("Введите первое число: "))
                second_number = int(input("Введите второе число: "))

        elif user_choice == "4":
            if second_number == 0:
                print("Учи матчасть. На ноль делить нельзя")
                second_number = int(input("Введите второе число: "))
            else:
                print(first_number / second_number)
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
                    first_number = int(input("Введите первое число: "))
                    second_number = int(input("Введите второе число: "))


fun2()
