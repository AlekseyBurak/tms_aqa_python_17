def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number
number = 369855
reverse_number = reverse_number(number)
print(f"Число : {number} наоборот : {reverse_number}")