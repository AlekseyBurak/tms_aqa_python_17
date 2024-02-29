def decorator(func):
    def wrapper(*args):
        result = func(args)
        print(result)
        print(reversed(result))

    return wrapper
@decorator
def calc_many(*args):
    print()
    print(*args)
    return sum(args)

calc_many(1, 5, 8, 9, 12)



