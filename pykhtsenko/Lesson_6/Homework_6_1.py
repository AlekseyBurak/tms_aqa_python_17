def count_symbols(input_string):
    symbol_count = {}
    result_string = " "
    for symbol in input_string:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1
    for char, count in symbol_count.items():
        result_string += char + str(count)
    return result_string
input_string = input("Input text: ")
result = count_symbols(input_string)
print(result)