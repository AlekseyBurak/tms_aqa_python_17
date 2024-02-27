

def reverse_num(number: int) -> int:
    """
    Takes a positive integer and return it's reversed version
    :param number:
    :return:
    """
    if number < 0:
        print("Positive numbers only")
        raise ValueError
    else:
        list_num = list(str(number))[::-1]
        list_num.reverse()
        reverse_int = int(''.join(list_num))
        print(reverse_int)
        return reverse_int


