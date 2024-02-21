def calculator() -> int:
    while True:
        operation = int(input("Select a command from 1 to 5. \n"))
        first_value = int(input("Enter the first value \n"))
        second_value = int(input("Enter the second value \n"))
        if operation == 1:
            print(first_value + second_value)
        elif operation == 2:
            print(first_value - second_value)
        elif operation == 3:
            print(first_value * second_value)
        elif operation == 4:
            if second_value == 0:
                print("На ноль делить нельзя!")
                break
            print(first_value / second_value)
        elif operation == 5:
            print("you chose 5")
            break

print(calculator())