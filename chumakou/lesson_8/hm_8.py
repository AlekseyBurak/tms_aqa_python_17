def decorator(conversion_type: callable()):

    def wrapper(func):

        def inner(*args):
            new_args = map(conversion_type, args)
            result = func(new_args)
            print(result)
            return result

        return inner()

    return wrapper()

@decorator(conversion_type=float)
def calc(a,b):
    return a + b

calc(5,5)
