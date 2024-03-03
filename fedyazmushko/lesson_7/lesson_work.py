# def revers_num(number: int) -> int:
#     """
#     Takes a positive integer and return it's reversed version
#     :param number:
#     :return:
#     """
#     if number < 0:
#         print("Positive number only")
#         return
#     else:
#         list_num = list(str(number))
#         list_num.reverse()
#         reverse_int = int(''.join(list_num))
#         print(reverse_int)
#         return reverse_int
#
#
# revers_num(12345)
# import time
#
#
# def outer_function():
#     x = time.time()
#     def inner_function():
#          y = time.time()
#         return y - x
#
#     return inner_function
#
#
# closure = outer_function()
# time.sleep(5)
# print(closure())

# def my_sum(x, y):
#     return x + y
#
# def calc(x, y, func ):
#     return func(x, y)
#
# print(calc(10, 5, my_sum))



# def my_func(x):
#     return x ** 2

# f = lambda x: x ** 2
# print(f(4))


# my_list = [1, 2, 3, 4, 5, 4, 2, 9, 5, 4]


# map_str = map(lambda x:  x ** 2 / x ** 3 , my_list)
# print(list(map_str))


# my_filter = filter(lambda x: x<5, my_list)
#
# print(list(my_filter))



# my_list = ["aaaaa", 'aaaaa', "aa", 'aaa', 'aaaaaaaaaaa', 'aaaa', 'aaaaaaaaa', 'aa']
#
#
# my_filter = filter(lambda x: len(x) < 5, my_list)
# print(list(my_filter))


# my_dict = { "a": 1, "b": 2, "c": 3}
# my_filter = filter(lambda k:  k[1] < 3, my_dict.items())
# print(list(my_filter))
# for k, v in my_dict.items():
#     print(f' {k=}: {v=}')


# try:
#     res = 10 / 1
#     print(res)
#
# except ZeroDivisionError:
#     print('no zeroes')
#
# except TypeError:
#     print('Only integers')
#
# else:
#     print('No problems')
#
# finally:
#     print('I will work in any case')

# try:
#     air = False
#     turn_on_air()
#     air = True
#
# finally:
#     if air:
# turn_off_air()

rost = [165, 163, 162, 160, 157, 157, 155, 154]
