# # beautiful, but not effective decision
# def flatten(init_list: list, storage: list):
#     for element in init_list:
#         if isinstance(element, list):
#             flatten(element, storage)
#         else:
#             storage.append(element)
#     print(storage)
#
# init_list = [1, 2, [2], 7, [3, 6, 2], [5, 34, [4, [5, [2, 1, [10]]]]]]
# storage = []
# flatten(init_list, storage)
#
# def flatten_nested_array(nested_array):
#
#     flat_list = []
#     i = 0
#     while i < len(nested_array):
#         if isinstance(nested_array[i], list):
#             nested_array = nested_array[:i] + nested_array[i] + nested_array[i+1:]
#             # print(nested_array[:i])
#             # print(nested_array[i])
#             # print(nested_array[i+1:])
#             # print('+++++++++')
#             # print(nested_array)
#             # print('+++++++++')
#         else:
#             i += 1
#     for item in nested_array:
#         flat_list.append(item)
#     return flat_list

###########

def my_func(x):

    def hello(y):
        return x + y

    return hello

# print(my_func(5)(6))
# inner = my_func(5)
# print(inner(6))

def my_func2():
    print("hello from func2")
# def my_func3(func):   # decorator
#
#     def wrapper():
#         print("one")
#         func()
#         print("two")
#     return wrapper()
#
# my_func2() = my_func3(my_func2)
#
# my_func2()

# def my_func3(func):   # decorator
#
#     def wrapper():
#         print("one")
#         func()
#         print("two")
#     return wrapper()
#
# @my_func3
# def my_func2():
#     print("hello from func 2")
#
# my_func2()
#
# def decorator(func):
#
#     def wrapper(*args, **kwargs):
#         print("Sum of numbers")
#         print(f"Args -- {args}")
#         print(func(*args, **kwargs))
#     return wrapper
#
# @decorator
# def calc_all(*args):
#     # sum(args1)
#
#     print()
#     print(*args)
#     return sum(args)
#
# calc_all(1, 2, 3, 4, 5)


def decorator(func):

    def wrapper(*args):

        result = func(*args)
        print(result)
        result.reverse()
        print(result)
    return wrapper

@decorator
def sort(*args):
    return sorted(args)
sort(*range(2, 50, 5))

number_names = {
    	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    	10: 'ten', 11: 'eleven', 12: 'twelve',
    	13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}