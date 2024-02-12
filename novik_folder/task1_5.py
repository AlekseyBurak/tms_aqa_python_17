import math

leg_triangle_1 = int(input("Enter the first value \n"))
leg_triangle_2 = int(input("Enter the second value \n"))

hypotenuse_sqrt = leg_triangle_1 ** 2 + leg_triangle_2 ** 2
hypotenuse = math.sqrt(hypotenuse_sqrt)

square = (leg_triangle_1 * leg_triangle_2) / 2

print(f'Hypotenuse is {hypotenuse} and Square is {square}')