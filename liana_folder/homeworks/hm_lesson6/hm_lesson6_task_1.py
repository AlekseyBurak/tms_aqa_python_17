text = input().lower()
def func1(text: str) -> str:
    new_text = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            new_text += text[i-1] + str(count)
            count = 1
    new_text += text[-1] + str(count)
    return new_text

result = func1(text)
print(result)
