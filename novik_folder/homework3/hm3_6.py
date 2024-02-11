import math

single_character = (input('Enter your single character \n'))
new_character = ord(single_character)
amount = len(str(new_character))
result = math.sqrt(new_character)/amount
print(result)
