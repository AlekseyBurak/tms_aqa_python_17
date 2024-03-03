def the_required_line(stroka):
    compressed = ""
    count = 1
    for _ in range(len(stroka) - 1):
        if stroka[_] == stroka[_ + 1]:
            count += 1
        else:
            compressed += stroka[_] + str(count)
            count = 1
    compressed += stroka[-1] + str(count)
    return compressed

print("Введите любое слово")
input_string = str(input())
result = the_required_line(input_string)
print(result)
