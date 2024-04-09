import math
while True:
    try:
        a = float(input("Enter first value\n"))
        b = float(input("Enter second value\n"))
        average_a = float(a+b)/2
        average_b = float(a*b)**(1/2)
        print("Среднее арифметическое = ", average_a, "среднее геометрическое = ", average_b)
        break
    except ValueError:
        print("Please enter number values.")