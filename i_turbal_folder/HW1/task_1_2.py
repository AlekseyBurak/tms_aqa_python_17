import math

while True:
    try:
        x = float(input("Enter X\n"))
        y = float(input("Enter y\n"))
        test1 = float((abs(x)+abs(y))/(1+(abs(x*y))))
        print('Result:', round(test1, 2))
        break
    except ValueError:
        print("Please enter number values.")

