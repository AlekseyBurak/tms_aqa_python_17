def func(name: str) -> str:
    """
    This func will greet you person
    :param name:
    :return:
    """
    return f"Hello {name}"



def sum_all(*args: int) -> int:
    """
    Sum all
    :param args:
    :return:
    """

    sum = 0
    for i in args:
        sum += i
    return sum