def decorator(types):
    def wrapper(func):
        def inner(*args):
            new_args = []
            new_str = ""
            for i in args:
                if types == "int":
                    i = int(i)
                    new_args.append(i)

                elif types == "float":
                    i = float(i)
                    new_args.append(i)

                elif types == "str":
                    new_str += str(i)

            print(new_str if types == "str" else sum(new_args))

        return inner

    return wrapper


@decorator("int")
def func(*args):
    return


func(5, "52", "-3")
