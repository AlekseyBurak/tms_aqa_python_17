# фукнции

# def func(zp, currency):
#     return zp / currency
#
# # print(func(10_000, 3.23))
# print(func(10_000, currency=3.23))


# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# func(1,2,3,4, {"a": 1}, name="alex", age="30", day="today", question="good")
#


# def func(name: str) -> str:
#
#     return f"Hello {name}"
#

def func(*args: int) -> int:
    summ = 0
    for item in args:
        summ += item
    return summ

print(func(1,2,3,4))