def flatten(list_example: list, flatten_list: list) -> list:
    """
    This function flattens the list.
    :param list_example: non-flatten list
    :param flatten_list: flatten list
    :return: flatten list
    """
    for i in list_example:
        if type(i) is list:
            flatten(i, flatten_list)
        else:
            flatten_list.append(i)

    return flatten_list


def main():
    """
    This function calls a function to flatten the list.
    """
    list_example = [1, 2, [2], 7, [3, 6, 2], [5, 34, [4, [5, [2, 1, [10]]]]]]
    flatten_list = []

    print(flatten(list_example, flatten_list))


main()
