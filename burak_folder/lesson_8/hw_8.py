

def decorator(conversion_type: callable):
    """
    :param conversion_type:
    :return:
    """

    def wrapper(func):

        def inner(*args):
            new_args = map(conversion_type, args)
            result = func(*new_args)
            return result

        return inner

    return wrapper


@decorator(str)
def calc(*args):
    result = args[0]
    for elem in args[1:]:
        result += elem
    return result


