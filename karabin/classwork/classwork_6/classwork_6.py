# def func():
#     a = 1 + 1
#     return a
# print(func())

# def func(zp, currency):
#     return zp / currency
# print(func(10_000, 3.23))

# def func(zp: int, currency: int):
#     """
#
#     :param zp:
#     :param currency:
#     :return:
#     """
#     return zp / currency
# print(func(10_000, 3.23))

# def func(zp: int, currency: int = 2.0):
#     """
#
#     :param zp:
#     :param currency:
#     :return:
#     """
#     return zp / currency
# print(func(10_000))

# def func(a: int, my_list: list = []):
#     my_list.append(a)
#     print(my_list)
# func(5)
# func(6)
# func(7)

# def func(*args, my_list: list = None):
#     if not my_list:
#         my_list = []
#     my_list.append(args)
#     print(my_list)
# func(1, 2, 3,6,"strint", [1,2,3], my_list=['start'])

# def func(my_list: list = None, **kwargs):
#     if not my_list:
#         my_list = []
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")
#     print(my_list)
# func(my_list=["start"], name="Aleksandr", age=39, day="today")


# def func(*args: int) -> int:
#     """
#     Sum all
#     :param args:
#     :return:
#     """
#     return sum(args)
# print(func(1, 2, 3, 4))



# communalka = 10_000 / 3.23 * .3
# eda = 10_000 / 3.23 * .2
# zanachka = 10_000 / 3.23 * .4
# party = 10_000 / 3.23 * .1

# def func_position(first, second, /, third):
#     """
#     :param first: only positional
#     :param second: only positional
#     :param third: may be either positional or key-word
#     :return:
#     """
#     pass


# только именованные справа от символа *
# слева можно именованые или позиционные
#
# def func_key_word(first, second, *, third):
#     """
#     :param first: may be either positional or key-word
#     :param second: may be either positional or key-word
#     :param third: only key-word
#     :return:
#     """
#     pass
#
#
# def func_args_example(*args):
#     """
#     Try this func
#     :param args: as many positional arguments as you want
#     :return:
#     """
#     for item in args:
#         print(f"This is one of the elements from args -- {item}")


# def func_kwargs_example(**kwargs):
#     """
#     Try this func
#     :param kwargs: as many key-word arguments as you want
#     :return:
#     """
#     for key, value in kwargs.items():
#         print(f"This is one of the key-value pairs from kwargs -- {key}: {value}")