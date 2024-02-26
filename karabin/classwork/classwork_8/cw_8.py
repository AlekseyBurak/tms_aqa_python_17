# def my_funk3(func):
#
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
#     return "SOME STR FOR RETURN"
#

# another_example

# def decorator(func):
#
#     def wrapper(a, b):
#         print("Sum of numbers")
#         print(func(a, b))
#
#     return wrapper
#
# @decorator
# def calc(a, b):
#     return a + b
#
# calc(20, 30)


# another_example
# def decorator(func):
#
#     def wrapper(*args):
#         print("Sum of numbers")
#         print(f"Args -- {args}")
#         print(func(*args))
#
#     return wrapper
#
# @decorator
# def calc(a, b):
#     return a + b
#
# calc(20, 30)
#
# @decorator
# def calc_many(a, b, c):
#     return a + b + c
#
# calc_many(1, 2, 3)
#
# def calc_very_much(*args):
#     print()
#     print(*args)
#     return sum(args)
#
# calc_very_much(6, 7, 8)

# one_more_example
# number_names = {
#     	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#     	10: 'ten', 11: 'eleven', 12: 'twelve',
#     	13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}
# На вход подаётся некоторое количество (не больше сотни) разделенных пробелом целых чисел
# (каждое не меньше 0 и не больше 19).
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается
# позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)


# def decorator(func):
#
#     def wrapper(*args):
#         lst = func(*args)
#         print(f"Args -- {args}")
#         print(sorted(lst))
#         lst.reverse()
#         print(lst)
#
#     return wrapper
#
# @decorator
# def srt(*args):
#     return sorted(args)
#
# srt(15, 16, 9, 6, 25, 14)

