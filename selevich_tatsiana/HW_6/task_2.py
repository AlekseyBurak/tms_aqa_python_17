def validate_user_option(user_input: str) -> str:
    """
    This function validates the user's choice of math operations option.
    :param user_input: user option
    :return: validated user option
    """
    while not user_input.isdigit() or user_input not in ['1', '2', '3', '4', '5']:
        print("\nError: The input value should be digit\n")
        user_input = input("Select option: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Exit: ")

    return user_input


def validate_first_number(first_number: str) -> float:
    """
    This function validates the user's first number.
    :param first_number: first number
    :return: validated first number
    """
    while not first_number.isdigit():
        print("\nError: The input value should be digit\n")
        first_number = input("Enter the first number: ")

    return float(first_number)


def validate_second_number(second_number: str, user_input: str) -> float:
    """
    This function validates the user's second number.
    :param second_number: second number
    :param user_input: user option
    :return: validated second number
    """
    while (not second_number.isdigit()) or (second_number.isdigit() and float(second_number) == 0 and user_input == '4'):
        if not second_number.isdigit():
            print("\nError: The input value should be digit\n")
        else:
            print("Error: You cannot divide by zero")

        second_number = input("Enter the second number: ")

    return float(second_number)


def addition(first_number: float, second_number: float) -> float:
    """
    This is an addition function.
    :param first_number: first number
    :param second_number: second number
    :return: sum
    """
    return first_number + second_number


def subtraction(first_number: float, second_number: float) -> float:
    """
    This is a subtraction function.
    :param first_number: first number
    :param second_number: second number
    :return: difference
    """
    return first_number - second_number


def multiplication(first_number: float, second_number: float) -> float:
    """
    This is a multiplication function.
    :param first_number: first number
    :param second_number: second number
    :return: product
    """
    return first_number * second_number


def division(first_number: float, second_number: float) -> float:
    """
    This is the division function.
    :param first_number: first number
    :param second_number: second number
    :return: quotient
    """
    return first_number / second_number


def main():
    user_input = 0

    while user_input != 5:
        user_input = input("Select option: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Exit: ")

        if user_input == '5':
            print("Game over!")
            break

        user_input = validate_user_option(user_input)

        first_number = input("Enter the first number: ")
        first_number = validate_first_number(first_number)

        second_number = input("Enter the second number: ")
        second_number = validate_second_number(second_number, user_input)

        if user_input == '1':
            print(f"Result = {addition(first_number, second_number)}")
        elif user_input == '2':
            print(f"Result = {subtraction(first_number, second_number)}")
        elif user_input == '3':
            print(f"Result = {multiplication(first_number, second_number)}")
        elif user_input == '4':
            print(f"Result = {division(first_number, second_number)}")


main()
