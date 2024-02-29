# def decorator(func):
#
# import time
#
#
# def my_func(x):
#     """
#     Пример замыкания
#     :param x:
#     :return:
#     """
#
#     def hello(y):
#         return x + y
#
#     return hello
#
# inner = my_func(5)
# print(inner(6))
#
# def my_funk2():
#     return 2 + 2
#
# def my_func3(func):
#     """
#     Пример функции высшего порядка
#     :param func:
#     :return:
#     """
#     print("start")
#     print(func())
#     print("finish")
#
# my_func3(my_funk2)
#
#
# def my_funk2():
#     print("hello from funk 2")
#
#
#
# def decorator(func):
#     """
#     Декоратор
#     :param func:
#     :return:
#     """
#
#     def wrapper():
#         """
#         Функия обертка - оборачивает функцию к которой применяется декоратор
#         :return:
#         """
#         print("Some optional step before func")
#         result = func()  # Some func work
#         print("Some optional step after func")
#         return result  # return func work
#
#     return wrapper  # return wrapper
#
#
# @decorator
# def my_funk2(name):
#     return f"SOME STR FOR RETURN {name}"
#
#
#
# def decorator(func):
#     """
#     Пример с передачей аргументов в декорируемую функцию
#     :param func:
#     :return:
#     """
#
#     def wrapper(*args):
#
#         result = func(*args)
#
#         print(result)
#         rev = result.copy()
#         rev.reverse()
#         print(rev)
#
#     return wrapper
#
#
# @decorator
# def calc_many(*args):
#     return sorted(args)
#
# calc_many(23, 52, 234, 3, 758, 34, 6, 958)
#
#
# def decorator(sleep_time: int):
#     """
#     Пример с передачей аргументов в декоратор
#     :param sleep_time:
#     :return:
#     """
#
#     def wrapper(func):
#
#         def inner(*args):
#             print("I'll try")
#             result = func(*args)
#             print('I failed')
#             time.sleep(sleep_time)
#             return result
#
#         return inner
#
#     return wrapper
#
#
# @decorator(5)
# def calc(a, b):
#     return a + b
#
#
#
#def decorator(func):
#
#     def wrapper():
#         print("Some optional step before func")
#         result = func()  # Some func work
#         print("Some optional step after func")
#         return result  # return func work
#
#     return wrapper  # return wrapper
#
#
# @decorator
# def my_funk2(name):
#     return f"SOME STR FOR RETURN {name}"
#
#
# def my_funk3(func):
#     def wrapper():
#         print("one")
#         result = func()
#         print("two")
#         return result
#
#     return wrapper
#
# @my_funk3
# def my_funk2():
#     return "NEW WORD"
#
# s = my_funk2()
# capital_s = s.lower()
# print(capital_s)