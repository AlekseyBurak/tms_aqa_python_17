#Реализуйте программу, которая спрашивала у пользователя, какую операцию
# он хочет произвести над числами, а затем запрашивает два числа и выводит результат
# Проверка деления на 0

def main():
    operation = input("Select an operation (+, -, *, /, exit): ")
    num1 = float(input("Enter a number 1: "))
    num2 = float(input("Enter a number 2: "))
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "exit":
        result = "Stop counting!!"
    else:
        print("Invalid operation. Please choose from +, -, *, /, exit.")
        return
    print(f"Результат: {result}")

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: division by zero.")
        return None
main()