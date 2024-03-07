
def decor(type1):
    def wrapper(func):
        def inner(*args):
            converted = []
            # converted = [type1(i) for i in args]

            for i in args:
                if type(i) is type1:
                    converted.append(i)
                else:
                    converted.append(type1(i))
                return func(*args)
            # print(f"Adding of params {args} is {func(*args)}")

        return inner
    return wrapper

@decor(type1=int)
def add_symbols(*args):
    s1 = sum(args)
    return s1
@decor(type1=str)
def add_symbols2(*args):
    s2 = "".join(args)
    return s2

print(add_symbols(2, 4, 5, 6))
# print(add_symbols(2, 4, 5, 6, '7'))

print(add_symbols2("a", "b", "c"))
# print(add_symbols2("a", "b", "c", 7))
