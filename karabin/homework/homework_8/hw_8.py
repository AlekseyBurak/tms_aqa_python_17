# """
# Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
#
# @typed(type=’str’)
# def add_two_symbols(a, b):
#     return a + b
#
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’
#
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#     return a + b + с
#
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001
#
#
#
# Тип параметров проверяйте как удобно. Колиество аргументов в функции - минимум 2. В иделале через *args
# """
#
def decorator():
    def wrapper(func):

        def inner(*args, **kwargs):
            print("Let`s try")
            lst = func(*args, **kwargs)
            print(lst)
            if isinstance(lst, str):
                return "".join(lst)
            elif isinstance(lst, float):
                return lst
            elif isinstance(lst, int):
                return lst
            else:
                print("Try one more time")
            return lst

        return inner

    return wrapper


@decorator()
def calc(a, b):
    return a + b


calc(3, 2)


@decorator()
def calc_letters(a, b):
    return a + b


calc_letters("a", "b")


@decorator()
def calc_three_letters(a, b, c):
    return a + b + c


calc_three_letters("a", "b", "c")


@decorator()
def calc_float(a, b, c):
    return a + b + c


calc_float(0.1, 2.1, 3.789)

print("I did it")
