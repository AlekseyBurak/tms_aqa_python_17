"""
Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:

@typed(type=’str’)
def add_two_symbols(a, b):
    return a + b

add_two_symbols("3", 5) -> "35"
add_two_symbols(5, 5) -> "55"
add_two_symbols('a', 'b') -> 'ab’

@typed(type=’int’)
def add_three_symbols(a, b, с):
    return a + b + с

add_three_symbols(5, 6, 7) -> 18
add_three_symbols("3", 5, 0) -> 8
add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001



Тип параметров проверяйте как удобно. Колиество аргументов в функции - минимум 2. В иделале через *args
"""

def decorator(x_type): # Здесь нужно принимать аргумент, который говорил, какие типы даннных складываем.

    def inner(func):

        def wrapper(*args):
            # здесь реалтзовать проверку и при необходимости приведение к переданному типу данных
            i_args = []
            for arg in args:
                if isinstance(arg, x_type):
                    i_args.append(arg)
                else:
                    i_args.append(x_type(arg))
            #result = func(*x_type)
            #return result
            return func(*i_args)

        return wrapper

    return inner


# @decorator() # здесь он передается
@decorator(str)
def calc(a, b):
    print(a + b)
    #return a + b

@decorator(int)
def many_calc(a, b, c):
    print(a + b + c)

@decorator(str)
def str4_calc(a, b, c, d):
    print(a + b + c +d)

calc('sd', 'al')
many_calc(2, 3, 5)
str4_calc('По', 'ех', 'ал','и!')