def my_funx(text) -> str:
    """

    :param text:
    :return:
    """
    currency_char = ''
    changed_str = ''
    my_counter = 0
    for char in text:
        if char == currency_char: # проверяем является ли символ предыдущим
            my_counter += 1
        else:
            if my_counter > 1:
                changed_str += currency_char + str(my_counter)
            else:
                changed_str += currency_char
            my_counter = 1
            currency_char = char
    if my_counter > 1:
        changed_str += currency_char + str(my_counter)
    else:
        changed_str += currency_char
    return changed_str



input_text = input("Enter str\n")
result = my_funx(input_text)
print("Result:", result)


