# from itertools import groupby
#
# def count_of_all_letters(string):
#     letters = "".join([f"{i}{len(list(j))}" for i, j in groupby(string)])
#     print(letters)
# string = input("Enter_your_nonsense:\n ", )
# count_of_all_letters(string)


# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Проверка деления на 0.
#
# Пример
# Выберите операцию:
#     1. Сложение
#     2. Вычитание
#     3. Умножение
#     4. Деление
#     5. Выход
# Введите номер пункта меню:
# >>> 4
# Введите первое число:
# >>> 10
# Введите второе число:
# >>> 3
#
def calculations():
    choice = (input("Make your choice:\n"
                        "1. sum\n"
                        "2. diff\n"
                        "3. mul\n"
                        "4. div\n"
                        "5. stop\n"
                        "Do it: "))
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == "1":
        calc = summ(a, b)
    elif choice == "2":
        calc = diff(a, b)
    elif choice == "3":
        calc = mul(a, b)
    elif choice == "4":
        calc = div(a, b)
    elif choice == "5":
        calc = "Wrong choice"
    else:
        print("Try again")
        return
    print(f"Result: {calc}")

def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b != 0:
        return a / b
    else:
        print("Wrong number")


calculations()
