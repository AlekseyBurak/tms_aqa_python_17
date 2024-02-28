def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return "".join(args)
        elif isinstance(result, int):
            return result
        else:
            raise TypeError("Error!!")
    return wrapper

@decorator
def sum_numbers_letters(a, b, c):
    return a + b + c

result_args = sum_numbers_letters(1, 20, -55)
print(result_args)

result_letters = sum_numbers_letters("Home", "Work", "done")
print(result_letters)


