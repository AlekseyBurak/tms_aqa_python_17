
import sys

def encode(text, shift):
    text = text.lower()
    min_bound = 96
    max_bound = 122
    result = ""
    for char in text:
        char_kod = ord(char) + shift
        if char_kod > max_bound:
            char_kod = min_bound + shift - (max_bound - ord(char))
        result = result + chr(char_kod)
    return result


def decode(text, shift):
    text = text.lower()
    min_bound = 97
    max_bound = 123
    result = ""
    for char in text:
        char_kod = ord(char) - shift
        if char_kod < min_bound:
            char_kod = max_bound - shift - (min_bound - ord(char))
        result = result + chr(char_kod)
    return result


text = str(input('Enter your cipher: '))
if not text.isalpha():
    print('Enter the letters of the English alphabet')
    sys.exit()
shift = int(input('Enter your chift from 1 to 25:'))
if shift < 1 or shift > 25:
    print('Error: Enter your chift from 1 to 25')
    sys.exit()
direction = int(input('Chouse encode or decode: \n1 - encode \n2 - decode'))
result = ""
if direction == 1:
    result = encode(text, shift)
elif direction == 2:
    result = decode(text, shift)
else:
    print("error: invalid operation")
    sys.exit()

print(result)

