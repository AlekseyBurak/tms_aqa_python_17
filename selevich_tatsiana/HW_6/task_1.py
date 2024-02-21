def handle_last_character(elem: str, previous_elem: str, i: int, compressed_list: list[int | str]) -> None:
    """
    This function processes the last character in the string and adds it to compressed list.
    :param elem: current element
    :param previous_elem: previous element
    :param i: counter
    :param compressed_list: compressed list
    """
    if elem == previous_elem:
        compressed_list.append(elem)
        compressed_list.append(i)
    else:
        compressed_list.append(elem)


def compare_characters(elem: str, next_elem: str, i: int, compressed_list: list[int | str]) -> int:
    """
    This function compares the current and next character and adds it to a compressed list.
    :param elem: current element
    :param next_elem: next element
    :param i: counter
    :param compressed_list: compressed list
    :return: number of character repetitions
    """
    if elem == next_elem:
        i += 1
        return i
    else:
        compressed_list.append(elem)
        if i != 1:
            compressed_list.append(i)
        return 1


def main():
    """
    This function converts a string.
    Example: "cccbba" == "c3b2a"
    """
    user_input = input("Enter a string: ")

    compressed_list = []
    i = 1

    for ind, elem in enumerate(user_input):
        if len(user_input) == 1:
            compressed_list.append(elem)
            break

        if ind == len(user_input) - 1:
            handle_last_character(elem, user_input[ind - 1], i, compressed_list)
            break

        i = compare_characters(elem, user_input[ind + 1], i, compressed_list)

    formatted_compressed_list = list(map(str, compressed_list))

    print(f"Result: {"".join(formatted_compressed_list)}")


main()
