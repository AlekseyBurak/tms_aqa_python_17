def crazy_calculator() -> int:
    print("""
    Select an operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Exit
    """)
    action = int(input("Enter an operation: "))
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    while action > 5 or action <= 0:
        print("something's wrong, try again..")
        action = int(input("Enter an operation: "))
    if action == 1:
        result = num1 + num2
    elif action == 2:
        result = num1 - num2
    elif action == 3:
        result = num1 * num2
    elif action == 4:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "something's wrong, can't divide by zero"
    elif action == 5:
        result = "Bue!"

    print("Result:", result)
    return result

crazy_calculator()
