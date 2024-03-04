#задача из дз №8
def decorator(type: callable):

    def wrapper(func):

        def inner(*args):
            new_args = map(type, args)
            result = func(*new_args)
            print(result)
            return result

        return inner

    return wrapper

# @decorator(type=str)


def add_symbols(*args):
    res = args[0]
    for i in args[1:]:
        res += i
    return res
#
#
# add_symbols(7, '6', 654, 85)


(decorator(type=str))(add_symbols)(7, '6', 654, 85.7)
(decorator(type=int))(add_symbols)(7, '6', 654, 85.7)
(decorator(type=float))(add_symbols)(7, '6', 654, 85.7)

#задача про линии
class Liniya:
    def __init__(self, linea1: int, linea2: int):
        self.linea1 = linea1
        self.linea2 = linea2

    def dlina(self):
        res = self.linea1 + self.linea2
        return res


linea_sum = Liniya(5, 9)
f = linea_sum.dlina()
print(f'Длина отрезка равна {f}')