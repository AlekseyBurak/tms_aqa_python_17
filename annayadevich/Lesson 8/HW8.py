def decorator(type):
    def wrapper(func):
        def inner(*args):
            converted_args = []
            for i in args:
                if isinstance(i, type):
                    converted_args.append(i)
                else:
                    converted_arg = type(i)
                    converted_args.append(converted_arg)
            result = func(*converted_args)    # распаковка элементов
            return result
        return inner
    return wrapper

@decorator(type=str)
def add_two_symbols_str(a, b):
    return a + b

@decorator(type=int)
def add_two_symbols_int(a, b):
    return a + b


print(add_two_symbols_str(5, 5))
print(add_two_symbols_int(5, 5))




















