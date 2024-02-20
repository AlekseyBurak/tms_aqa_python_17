def print_rules():
    print('Выберите операцию: '
          '1. Сложение '
          '2. Вычитание '
          '3. Умножение '
          '4. Деление '
          '5. Выход')


def read_operation():
    return int(input('Введите номер пункта меню: '))


def read_number(order):
    return int(input(f'Enter {order} number: '))


def summ(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def multi(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        return 'Division by 0 not allowed'
    return num1 / num2


def calculate(num1, num2, operation):
    if operation == 1:
        return summ(num1, num2)
    elif operation == 2:
        return sub(num1, num2)
    elif operation == 3:
        return multi(num1, num2)
    elif operation == 4:
        return div(num1, num2)
    else:
        return "Invalid operation"


while True:
    print_rules()
    operation = read_operation()
    if operation == 5:
        print('Exit')
        break
    num1 = read_number('first')
    num2 = read_number('second')
    print(f'Result: {calculate(num1, num2, operation)}')






