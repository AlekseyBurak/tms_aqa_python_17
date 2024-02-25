def validate_user_input(user_input: list[str]) -> list[str]:
    """
    This function validates user input.
    :param user_input: user input
    :return: validated user input
    """
    is_valid_user_input = False

    while not is_valid_user_input:
        for i in user_input:
            if not i.isdigit():
                print("Error: The input value should contain only numbers")

                is_valid_user_input = False
                user_input = input("Enter a list of numbers: ").split()
                break
            else:
                is_valid_user_input = True

    return user_input


def main():
    """
    This function returns all elements of a list that are greater than the previous one.
    """
    user_input = input("Enter a list of numbers: ").split()
    validated_user_input = validate_user_input(user_input)
    new_list = list(map(int, validated_user_input))

    result = []

    for ind, elem in enumerate(new_list):
        if ind == 0:
            continue
        elif elem > new_list[ind - 1]:
            result.append(elem)

    print(f"Result: {result}")


main()
