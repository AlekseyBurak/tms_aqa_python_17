

def letter_count(string: str) -> str:
    """
    This function takes a string and returns new strings with the letters and their counts.
    :param string:
    :return:
    """
    result = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            if count > 1:
                result += string[i] + str(count)
            else:
                result += string[i]
            count = 1
        if i == len(string) - 2:
            if string[i] != string[i + 1]:
                result += string[i + 1]
            else:
                result += string[i] + str(count)

    return result

#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


for s in ("cccbba", "abeehhhhhccced", "aaabbceedd", "abcde", "aaabbdefffff"):
    print(letter_count(s))


def calc() -> None:
    """
    This function takes no arguments and returns the result math calculation.
    math operation and operands are asked from the user.
    :return:
    """
    while True:
        command = input("""
        Выберите операцию:
            1. Сложение
            2. Вычитание
            3. Умножение
            4. Деление
            5. Выход
            """
        )
        if command not in list("12345"):
            print("Неверная команда")
            continue
        if command == "5":
            break
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        if command == "1":
            print(num1 + num2)
        elif command == "2":
            print(num1 - num2)
        elif command == "3":
            print(num1 * num2)
        elif command == "4":
            if num2 == 0:
                print("No zero division")
                continue
            print(num1 / num2)

calc()
