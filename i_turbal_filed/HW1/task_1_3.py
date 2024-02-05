import math
while True:
    try:
        edge = float(input('Enter cube edge'))
        if edge <= 0:
            print("Cube edge can't be less than 0 ")
        else:
            print("Cube valume =", edge**3, "area =", edge**2)
        break
    except ValueError:
        print("PLease enter number")
