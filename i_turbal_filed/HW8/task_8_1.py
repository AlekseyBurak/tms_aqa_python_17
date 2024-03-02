def decorator(x: str):
    """

    :param x: if x == '1' - str, if x=='2' - int, else return args
    :return:
    """
    def wrapper(func):
        def inner(*args):
            if x == '1':
                conversation = map(int, args)
                result = func(*conversation)
            elif x == "2":
                convesration = map(str, args)
                result = func(*convesration)
            else:
                result = args
            print(result)
            return result
        return inner
    return wrapper
@decorator(x= input("Enter value"))
def summ(*args):
    result = args[0]
    for i in args[1:]:
        result += i
    return result
summ(1,2)




