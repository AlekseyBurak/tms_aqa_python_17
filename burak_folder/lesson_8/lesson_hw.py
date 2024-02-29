def decorator(conversion_type: callable):

    def wrapper(func):

        def inner(*args, **kwargs):
            new_args = map(conversion_type, args)
            result = func(*new_args)
            print(result)
            return result

        return inner

    return wrapper


# @decorator(conversion_type=int)
def calc(*args):
    res = args[0]
    for item in args[1:]:
        res += item
    return res


(decorator(conversion_type=str))(calc)(9, "9", 789, 5.5)
(decorator(conversion_type=int))(calc)(9, "9", 789, 5.5)
(decorator(conversion_type=float))(calc)(9, "9", 789, 5.5)

