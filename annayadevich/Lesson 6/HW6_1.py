#Task_1 На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
def characters_count(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result_string = ""
    for char, count in char_count.items():
        if count == 1:
            result_string += char
        else:
            result_string += char + str(count)
    return result_string

input_string = input("Enter the characters: ")
result = characters_count(input_string)
print(result)

