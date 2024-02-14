lst = input("Enter 10 words: ").split()

while len(lst) != 10:
    print("Error: Enter 10 words")
    lst = input("Enter 10 words: ").split()

new_value = input("Enter a new value: ")

lst.insert(2, new_value)
del lst[6]

print(f"Updated list: {lst}")
