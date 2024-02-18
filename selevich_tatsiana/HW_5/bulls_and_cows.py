import random

numbers = list(range(10))
selected_numbers = random.sample(numbers, k=4)

while selected_numbers[0] == 0:
    selected_numbers = random.sample(numbers, k=4)

bulls = []
cows = []

while len(bulls) != 4:
    bulls = []
    cows = []

    user_input = input("Enter a four-digit number: ")

    while len(user_input) != 4 or not user_input.isdigit():
        print("Error: The input value should be four digits and contain only numbers")
        user_input = input("Enter a four-digit number: ")

    user_numbers = list(map(int, user_input))

    if selected_numbers == user_numbers:
        break
    else:
        for i in selected_numbers:
            ind = selected_numbers.index(i)
            elem_user = user_numbers[ind]

            if i == elem_user:
                bulls.append(i)
            elif i in user_numbers and i != elem_user:
                cows.append(i)

    print(f"Bulls = {len(bulls)}, cows = {len(cows)}")

print("You are winner!")
