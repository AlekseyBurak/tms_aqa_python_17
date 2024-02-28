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

def decorator(): # Здесь нужно принимать аргумент, который говорил, какие типы даннных складываем.

    def wrapper(func):

        def inner(a, b):
            # здесь реалтзовать проверку и при необходимости приведение к переданному типу данных
            result = func(a, b)

            return result

        return inner

    return wrapper


@decorator() # здесь он передается
def calc(a, b):
    return a + b
