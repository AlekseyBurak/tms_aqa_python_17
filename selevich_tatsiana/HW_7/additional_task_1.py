def validate_user_heights_input(user_heights_input: list[str]) -> list[str]:
    """
    This function validates user heights input.
    :param user_heights_input: user heights input
    :return: validated user heights input
    """
    is_valid_heights_input = False

    while not is_valid_heights_input:
        for i in user_heights_input:
            if not i.isdigit():
                print("Error: The input value should contain only numbers")

                is_valid_heights_input = False
                user_heights_input = input("Enter a list of students' heights: ").split()
                break
            else:
                is_valid_heights_input = True

    return user_heights_input


def validate_height_input(height_input: str) -> str:
    """
    This function validates height input.
    :param height_input: height input
    :return: validated height input
    """
    while not height_input.isdigit():
        print("Error: The input value should contain only numbers")
        height_input = input("Enter height: ")

    return height_input


def rank(heights: list[int], height: int) -> None:
    """
    This function outputs the index of the added height value.
    :param heights: heights
    :param height: height
    """
    for ind, elem in enumerate(heights):
        count = heights.count(height)

        if elem == height:
            heights.insert(ind + count, height)
            print(f"Added height index: {ind + count}")
        else:
            heights.append(height)
            heights.sort(reverse=True)
            print(f"Added height index: {heights.index(height) + count}")

        break


def main():
    """
    This function requests user input and calls the rank function.
    """
    user_heights_input = input("Enter a list of students' heights: ").split()
    validated_user_heights_input = validate_user_heights_input(user_heights_input)
    heights = list(map(int, validated_user_heights_input))

    heights.sort(reverse=True)

    height_input = input("Enter height: ")
    validated_height_input = validate_height_input(height_input)
    height = int(validated_height_input)

    rank(heights, height)


main()
