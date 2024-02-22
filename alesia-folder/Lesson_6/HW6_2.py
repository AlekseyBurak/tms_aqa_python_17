# task 2
print("Task 2")
print("Choose the operation below: \n 1. Addition \n 2. Subtraction "
      "\n 3. Multiplication \n 4. Division \n 5. Exit program")

def f2(n1: int, n2: int, n3: int):
    n1 = int(input("Write the number of chosen operation: "))
    while n1 != 5:
        if n1 >= 6:
            print("You can choose only 1, 2, 3, 4 or 5!")
            n1 = int(input("Write the number of chosen operation: "))
        else:
            n2 = int(input("Input 1st number: "))
            n3 = int(input("Input 2nd number: "))

            if n1 == 1:
                a = n2 + n3
                print("The result of addition is:", a)
                n1 = int(input("Write the number of chosen operation: "))
            elif n1 == 2:
                s = n2 - n3
                print("The result of subtraction is:", s)
                n1 = int(input("Write the number of chosen operation: "))
            elif n1 == 3:
                m = n2 * n3
                print("The result of multiplication is:", m)
                n1 = int(input("Write the number of chosen operation: "))
            elif n1 == 4:
                if n3 == 0:
                    while n3 == 0:
                        n3 = int(input("You cannot divide by 0! Input another number: "))
                else:
                    d = n2 / n3
                    print("The result of division is:", d)
                    n1 = int(input("Write the number of chosen operation: "))
            else:
                d = n2 / n3
                print("The result of division is:", d)
                n1 = int(input("Write the number of chosen operation: "))

    else:
        print("The end.")


f2(n1=input, n2=input, n3=input)
