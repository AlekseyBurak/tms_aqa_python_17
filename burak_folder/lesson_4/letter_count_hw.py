
my_string = input("Enter a string: ")

max_count = 0
max_char = None

for char in my_string.lower():
    if char.isalpha():
        count = my_string.count(char)
        if count > max_count:
            max_count = count
            max_char = char
        elif count == max_count and ord(char) < ord(max_char):
            max_count = count
            max_char = char
if not max_char:
    print("No letters in the string")
else:
    print(f"The most common character is {max_char} with {max_count} occurrences")