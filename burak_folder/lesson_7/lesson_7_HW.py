from typing import List, Tuple


def dash(char: str, step: int, encode: bool = True) -> int:
    """
    97 - a
    122 - z
    :param char:
    :param step:
    :param encode:
    :return:
    """
    result = None
    if encode:
        if (ord(char) + step) > 122:
            result = 96 + step - (122 - ord(char))
        else:
            result = ord(char) + step
    elif encode is False:
        if (ord(char) - step) < 97:
            result = 123 - step - (97 - ord(char))
        else:
            result = ord(char) - step
    return result


def caesar_kode(string: str, step: int, encode: bool = True) -> str:
    """
    Can encode and decode your string in latin
    :param string:
    :param step:
    :param encode:
    :return:
    """
    result = []
    for char in string.lower():
        if not char.isalpha():
            result.append(char)
        else:
            crypto_char = chr(dash(char, step, encode))
            result.append(crypto_char)
    print(''.join(result))
    return ''.join(result)

caesar_kode("zabcd!e", 1)
caesar_kode("abcde!f", 1, encode=False)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def where_piotr(students_height: List[int], piotr_height: int) -> Tuple:
    """
    Takes a list of student height and Piotr height, return Piotr index in human-readable form (not from 0 index)
    :param students_height:
    :param piotr_height:
    :return:
    """
    ordered_students, index = sorted(students_height), None
    ordered_students.reverse()
    for index in range(len(ordered_students)):
        if ordered_students[index] < piotr_height:
            ordered_students.insert(index, piotr_height)
            break

    return ordered_students, index + 1

print(where_piotr([165, 160, 162, 162, 154, 170, 158], 162))
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def give_me_more(init_list: List[int]) -> List:
    """

    :param init_list:
    :return:
    """
    result = list()
    for index in range(1, len(init_list)):
        if init_list[index] > init_list[index - 1]:
            result.append(init_list[index])
    print(result)
    return result


give_me_more(init_list=[1, 5, 2, 4, 3, 8, 6, 5, 3, 4, 5])

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def flatten(init_list: list, storage: list):
    for element in init_list:
        if isinstance(element, list):
            flatten(element, storage)
        else:
            storage.append(element)
    print(storage)


storage = []
init_list = [1, 2, [2], 7, [3, 6, 2], [5, 34, [4, [5, [2, 1, [10]]]]]]

flatten(init_list, storage)


def flatten_nested_array(nested_array):
    flat_list = []
    i = 0
    while i < len(nested_array):
        if isinstance(nested_array[i], list):
            nested_array = nested_array[:i] + nested_array[i] + nested_array[i+1:]
        else:
            i += 1
    for item in nested_array:
        flat_list.append(item)
    return flat_list


nested_array = [1, 2, [2], 7, [3, 6, 2], [5, 34, [4, [5, [2, 1, [10]]]]]]
flat_list = flatten_nested_array(nested_array)
print(flat_list)
