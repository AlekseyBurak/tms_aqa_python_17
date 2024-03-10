#
# def my_funk3(func):

#     def wrapper():
#         print("one")
#         result = func()
#         print("two")
#
#         return result
#
#     return wrapper
#
#
# @my_funk3
# def my_funk2():
#     return f"some str for return"
#
# # s = my_funk2()
# # capital_s = s.lower()
# # print(capital_s)
#


# def decorator(func):

#     def wrapper(*args, **kwargs):
#         print("Sum of numbers")
#         print(func(*args))
#
#     return wrapper
#
# @decorator
# def calc(a1, b1):
#     return a1 + b1
#
# calc(1,2)
#
# @decorator
# def calc_many(*args):
#     return sum(args)
#
# calc_many(1,2,3,4,5,6)

# import time
#
#
# def decoration(sleep_time: int):
#     def wrapper(func):
#         def inner(*args):
#             while True:
#                 try:
#                     print("I will try")
#                     result = func(*args)
#                 except:
#                     print("I failed")
#                     time.sleep(sleep_time)
#                 else:
#                      return result
#
#         return inner
#
#     return wrapper
#
# @decoration(1)
# def calc(a,b):
#     return a + b
#
# calc(1,2)


def decorator(func):
    def wrapper(*args):
        result = func(*args)
        print(result)
        rev = result.copy()
        rev.reverse()
        print(rev)

    return wrapper

@decorator
def calc_many(*args):
    return sorted(args)

calc_many(1,2,3,4,5)