def decorator(type):
    def wrapper(func):
        def inner(*args):
            if type == 'str':
                return func(*map(str, args))
            elif type == 'int':
                return func(*map(int, args))
        return inner
    return wrapper


@decorator('str')
def sum_str(*args):
    result = args[0]
    for i in args[1:]:
        result += i
    return result


@decorator('int')
def sum_int(*args):
    result = 0
    for i in args:
        result += i
    return result


print(sum_str(1, 1, 1))
print(sum_int('1', '1', '1'))
