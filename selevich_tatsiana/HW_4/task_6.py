text = input("Enter a text containing at least one letter: ").lower()
letters = []

for i in text:
    if i.isalpha():
        letters.append(i)

result = sorted(letters)

if len(result) == 0:
    print("Error: The text must contain at least one letter")
else:
    print("Result:", max(result, key=letters.count))
