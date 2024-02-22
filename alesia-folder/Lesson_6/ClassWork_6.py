
# currency = 3.23
# zp = 10_000

# communalka = zp / currency * .3
# eda = zp / currency * .2
# zanachka = zp / currency * .4
# party = zp / currency * .1

# def func():
#     a = 1 + 1
#     print(a)
    # return a

# print(func())
# print(func() + func() + func())

def  func1(zp, currency):
    """

    :param zp:
    :param currency:
    :return:
    """
    return zp / currency
print(func1(10_000, 3.23))
# print(func1(currency=3.23, zp=10_000))

def func2(zp: int, currency: int):
    return zp / currency

print(func2(10_000, 3.23))

def func3(zp: int, currency: int = 2.0):
    return zp / currency

print(func3(10_000))
print(func3(10_000, 4.0))

def func4(a: int, my_list: list = []):
    my_list.append(a)
    print(my_list)

func4(5)
func4(6)
func4(7)

# def func5(*args, my_list: list = None):
#     if not my_list:
#         my_list = []
#     my_list.append(args)
#     print(my_list)
#
# func5(*args: 1, 2, 3, 6, "strint", [1,2,3], my_list=["start"])

# def func6(my_list: list = None, **kwargs):
#     if not my_list:
#         my_list = []

def func7(*args1, **kwargs1):
    print(args1)
    print(kwargs1)
func7(1,2,3,4,5,6,7,{"a": 1}, name="Alex", age=30, day="toady", question="good")

def func8(a, b, c, *args, e = None, **kwargs):
    pass

func8(1, 2, 3, 1,2,3,4,55, e=34, name="me")

def func9(a, b, *, n):
    print("ok", a, b, n)
func9(1, 2, n="HERE")

# def func10(a, b, /, n):
#     print("ok", a, b, n)
# func10(1, 2, n="HERE")

def func11(name):
    print("Privet, ", name)
func11("Alesia")

def func12(name: str) -> str:
    """
    This func12 will greet you in person
    :param name: your nme
    :return: str
    """
    return f"Hello, {name}"

print(func12("Alesia"))


def func13(*args) -> int:
    summm = 0
    for item in args:
        summm += item
    return sum(args)

print(func13(5, 6, 7))




