# task 1

print(f"Original string -- {'www.my_site.com#about'}\n"
      f"Updated string -- {'www.my_site.com#about'.replace('#', '/')}")

print("=" * 50)  # Just a separator between tasks

# task 2
# Алеся сделала луше :)
print(f"Original word -- {(word:= input('Enter english verb to make Ving form --> '))}\n"
      f"Ving form (maybe not correct) -- {word + 'ing'}")

print("=" * 50)  # Just a separator between tasks

# task 3
print(f"Some extra spaces was added, wops -- |{(sentence := (' ' * 20) + input('Enter something --> ') + (' ' * 20))}|\n"
      f"Without extra spaces -- |{sentence.strip()}|")

print("=" * 50)  # Just a separator between tasks

# task 4
print(f"Here is your symbol from ASCII table by given code -- {chr(int(input('Give me some number in range 0-255 --> ')))}")

print("=" * 50)  # Just a separator between tasks

# task 5
print(f"Here is your symbol code from ASCII table by given symbol -- {(code := ord(input('Give me some latin letter  --> ')))}\n"
      f"And the answer for #6 task is -- {code ** .5 / len(str(code))}")

print("=" * 50)  # Just a separator between tasks


# task 7

number = int(input('Give me some xxxx number -- '))
unit = number % 10
tens = (number // 100) % 10
hundreds = (number % 100) // 10
thousands = number // 1000
print()
print(f"{thousands=}, {hundreds=}, {tens=}, {unit=}", sep='\n')

# same with while

print("=" * 50)  # Just a separator between tasks


number_while = int(input('Give me some xxxx number -- '))
count = 1
while number_while:
    digit = number_while % 10
    print(f"{count} digit is {digit}")
    count += 1
    number_while //= 10
