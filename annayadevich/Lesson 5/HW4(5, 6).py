# task 5
def find_unique_number(array1):
    unique_number = 0
    for num in array1:
        unique_number ^= num
    return unique_number

my_array = [1, 5, 2, 9, 2, 9, 1]
unique_number = find_unique_number(my_array)
print(f"Уникальное число в массиве: {unique_number}")

# task 6
text = ("Travelling is an, opportunity ! to learn 3 something new. "
        "While travelling 3 we have a ! great chance to acquire new - experience and knowledge. "
        "Someone practises 3 a foreign ! language, someone learns ! how to surf, someone, "
        "attends cooking, master classes8.")
text = text.lower()
letter_count = dict()

for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

most_common_letter = max(letter_count, key=letter_count.get)

print(f"The most common letter is: {most_common_letter}")