def calculator():
    operation = input("Выберите операцию (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print("Неверная операция!")
        return

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль")
        else:
            result = num1 / num2
            print("Результат:", result)
    elif operation == '+':
        result = num1 + num2
        print("Результат:", result)
    elif operation == '-':
        result = num1 - num2
        print("Результат:", result)
    elif operation == '*':
        result = num1 * num2
        print("Результат:", result)

calculator()