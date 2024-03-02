# def decorator(func):
#     def wrapper(*args):
#         result = func(*args) + 1
#         print(result)
#         return result
#     return wrapper
#
# @decorator
# def func_sum(*args: int):
#     return sum(args)
#
# func_sum(1,2,3,4,5)

# def decorator(fun):
#     def wrapper(name):
#         print(fun(name))
#         hello_name = fun(name)
#         print(hello_name.upper())
#         print(hello_name.lower())
#         print(hello_name[::-1])
#         return hello_name
#     return wrapper
#
# @decorator
# def hello(name:str):
#     return f"Hello {name}"
#
# hello("Payaso")


def decorator(func):
    def wrapper(*args):
        result = int(func(*args))
        print(result)
        return result
    return wrapper
@decorator
def func_func(x,y):
    return x >= y

x = int(input("X"))
y=int(input("y"))
func_func(x,y)