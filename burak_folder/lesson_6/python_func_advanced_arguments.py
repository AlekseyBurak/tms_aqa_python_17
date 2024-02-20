# только позиционные слева от символа /
# справа можно именованые или позиционные

def func_position(first, second, /, third):
    """

    :param first: only positional
    :param second: only positional
    :param third: may be either positional or key-word
    :return:
    """
    pass


# только именованные справа от символа *
# слева можно именованые или позиционные

def func_key_word(first, second, *, third):
    """

    :param first: may be either positional or key-word
    :param second: may be either positional or key-word
    :param third: only key-word
    :return:
    """
    pass


def func_args_example(*args):
    """
    Try this func
    :param args: as many positional arguments as you want
    :return:
    """
    for item in args:
        print(f"This is one of the elements from args -- {item}")


def func_kwargs_example(**kwargs):
    """
    Try this func
    :param kwargs: as many key-word arguments as you want
    :return:
    """
    for key, value in kwargs.items():
        print(f"This is one of the key-value pairs from kwargs -- {key}: {value}")