import math

first_number = int(input('Enter your first number \n'))
second_number = int(input('Enter your second number \n'))

average = (first_number + second_number)/2
geometric_mean = math.sqrt(first_number * second_number)
print(f'Average is {average} and Geometric mean is {geometric_mean}')