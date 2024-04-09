import math

while True:
    try:
        a = float(input('Enter a\n'))
        b = float(input('Enter b\n'))
        c = math.sqrt((a**2)+(b**2))
        S = 0.5*a*b
        if a < 0 or b < 0:
            print("Enter valuse more than 0 ")
        else:
            print("c =", c, "S =", S)
        break
    except ValueError:
        print("PLease enter numbers")
