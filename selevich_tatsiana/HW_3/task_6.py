character = input("Enter a character (in lower or upper case, only Latin): ")
code = ord(character)
print(f"Result: {code ** 0.5 / len(str(code))}")
