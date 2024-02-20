def numbers():
    number1 = float(input("Enter 1 number: "))
    number2 = float(input("Enter 2 number: "))
    return  number1, number2
def sum_numbers(number1, number2):
    return number1 + number2
def subtraction_numbers(number1, number2):
    return number1 - number2
def multiply_numbers(number1, number2):
    return number1 * number2
def division_numbers(number1, number2):
    if number2 !=0:
      return number1 / number2
    else:
        return "Error!!! It is not possible to divide by zero!!!!!!!"
print("Check action: \n", "1. Sum numbers\n", "2. Subtraction numbers\n", "3. Multiply numbers\n", "4. Division_numbers\n", "5. Escape")

choice = input("Input action(1/2/3/4/5): ")
if choice in ['1', '2', '3', '4', '5']:
    number1, number2 = numbers()
    if choice == '1':
        result = sum_numbers(number1, number2)
    elif choice == '2':
        result = subtraction_numbers(number1, number2)
    elif choice == '3':
        result = multiply_numbers(number1, number2)
    elif choice == '4':
        result = division_numbers(number1, number2)
    elif choice == '5':
        result = "Stop!!"
       # break

    print("Result: ", result)