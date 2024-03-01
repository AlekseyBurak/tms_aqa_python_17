def type_converter(type):
    def wrapper(func):
        def inner(a, b):
            if type == 'str':
                return func(str(a), str(b))
            elif type == 'int':
                return func(int(a), int(b))
        return inner
    return wrapper


@type_converter('str')
def sum_str(a,b):
    return a + b


@type_converter('int')
def sum_int(a, b):
    return a + b


print(sum_str(5, 9))
print(sum_int('5', '10'))






