import datetime as time
def decorator(func):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("summa:")
        print(f"Args -- {args}")
        rez =(func(*args, **kwargs))
        print(f"Среднее {rez / len(args)}")
        print(type(rez))
        print(f"Время расчета: {time.time() - start_time} секунд")

        return wrapper

# @decorator
# def calk(a1, b1):
#     return a1 + b1
#
# calk(145, 212)

@decorator
def calc_many(*args):
    print()
    print(*args)
    return sum(args)

calc_many(1, 2, 3, 125, 145)