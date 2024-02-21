# 1) На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"

def count_characters(string):

    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


string = str(input('Enter any string: '))
result = count_characters(string)
string_result = ''.join([f"{key}{value}" for key, value in result.items()])
print(string_result)