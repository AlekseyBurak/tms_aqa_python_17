def transform_args(elem_type: str):
    """
    This function checks the type of parameters used and converts if necessary.
    :param elem_type: element type
    """
    def wrapper(func):
        def inner(*args):
            new_args = []

            for i in args:
                if elem_type == "int":
                    new_args.append(int(i))
                elif elem_type == "str":
                    new_args.append(str(i))
                else:
                    raise TypeError("Unsupported data type (supported data types: str and int)")

            return func(*new_args)
        return inner
    return wrapper


@transform_args(elem_type="str")
def calculate_elements(*args: str | int) -> str | int:
    """
    This function adds elements (at least 2 elements).
    :param args: arbitrary number of elements
    :return: the result of addition of elements
    """
    sum_elem = args[0]

    if len(args) < 2:
        raise ValueError("The number of function arguments must be at least 2")

    for i in args[1:]:
        sum_elem += i

    return sum_elem


print(calculate_elements(5, 0, '7', 'fgj', 'dgh7'))
