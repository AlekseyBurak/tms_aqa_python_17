import random


def return_random_sample() -> list[int]:
    """
    This function returns a random sample of 4 non-repeating digits.
    :return: random sample
    """
    numbers = list(range(10))
    selected_numbers = random.sample(numbers, k=4)

    while selected_numbers[0] == 0:
        selected_numbers = random.sample(numbers, k=4)

    return selected_numbers


def validate_user_input(user_input: str) -> str:
    """
    This function validates user input.
    :return: validated user input
    """
    while len(user_input) != 4 or not user_input.isdigit():
        print("Error: The input value should be four digits and contain only numbers")
        user_input = input("Enter a four-digit number: ")

    return user_input


def define_bulls_and_cows(comp_numbers: list[int], user_numbers: list[int], bulls: list[int], cows: list[int]) -> None:
    """
    This function defines the number of bulls and cows.
    :param comp_numbers: comp numbers
    :param user_numbers: user numbers
    :param bulls: number of bulls
    :param cows: number of cows
    """
    for i in comp_numbers:
        ind = comp_numbers.index(i)
        elem_user = user_numbers[ind]

        if i == elem_user:
            bulls.append(i)
        elif i in user_numbers and i != elem_user:
            cows.append(i)


def main():
    """
    This function launches the "Bulls and Cows" game.
    The computer generates a secret 4-digit number with non-repeating digits.
    The player tries to guess this number.
    The computer reports back:
    - how many numbers were guessed without matching their positions (number of cows),
    - how many were guessed right up to the position (number of bulls).
    """
    comp_numbers = return_random_sample()

    bulls = []

    while len(bulls) != 4:
        bulls = []
        cows = []

        user_input = input("Enter a four-digit number: ")
        validated_user_input = validate_user_input(user_input)
        user_numbers = list(map(int, validated_user_input))

        if comp_numbers == user_numbers:
            break
        else:
            define_bulls_and_cows(comp_numbers, user_numbers, bulls, cows)

        print(f"Bulls = {len(bulls)}, cows = {len(cows)}")

    print("You are winner!")


main()
