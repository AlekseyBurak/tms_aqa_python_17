# def func(number: int) -> int:
#
#     if number < 0:
#         print("Enter another number")
#         raise ValueError
#     else:
#         string = list(str(number))
#         string.reverse()
#         reverse_int = int(''.join(string))
#         print(reverse_int)
#         return reverse_int
#
#
# func(321)

# my_list = [1, 2, 3, 4, 5, 4, 2, 9, 5, 4]
#
# map_str = map(lambda x: x ** 2 / x ** 3, my_list)
# print(list(map_str))

# my_list = [1, 2, 3, 4, 5, 4, 2, 9, 5, 4]
#
# my_filter = [x for x in my_list if x < 5]
# print(my_filter)
#
# my_list = [1, 2, 3, 4, 5, 4, 2, 9, 5, 4]

# def func(x):
#     return x < 5

# my_filter = filter(lambda x: x < 5, my_list)
# print(list(my_filter))

# string = ['asdadsads', 'asd', 'asdaa', 'asdasd']
# new_string = filter(lambda x: len(x) < 5, string)
# print(list(new_string))

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# my_filtered_dict = filter(lambda k: k[1] < 3, my_dict.items())
# print(list(my_filtered_dict))

# функция высшего порядка
# def my_sum(x, y):
#     """
#
#     :param x:
#     :param y:
#     :return:
#     """
#     return x + y
#
# def calc(x, y, func):
#     return func(x, y)
#
# print(calc(10, 5, my_sum))

# try, finally, except
# try:
#     res = 10 / 'a'
#     print(res)
# except ZeroDivisionError:
#     print('No zero')
# except TypeError:
#     print('Only integers')


# try:
#     res = 10 / 0
#     print(res)

# except ZeroDivisionError:
#     print('No zero')

# except TypeError:
#     print('Only integers')

# else:
#     print('No problems')

# finally:
#     print("I'll work in any case")

# account = None
# try:
#     account = create_account()
#
#
# finally:
#     delete_account

# my_list = [1, 2, [3, 4, [5, 6], 7], [8, [9, [10]]]]


