import random
import cowsay

digits = list(range(0, 10))

computer_number = [str(digits.pop(random.randrange(0, len(digits)))) for _ in range(4)]

print(computer_number)


HUMAN_MESSAGE = "Guess the 4-digit number with unique digits: "
INVALID_INPUT_WARNING = "You should enter 4-digit number with unique digits!"


while True:
    cows, bulls = 0, 0
    human_number = list(input(HUMAN_MESSAGE))

    input_check = True
    while input_check:
        if len(set(human_number)) != 4:
            print(INVALID_INPUT_WARNING)
            human_number = list(input(HUMAN_MESSAGE))
        if len(human_number) != 4:
            print(INVALID_INPUT_WARNING)
            human_number = list(input(HUMAN_MESSAGE))
        if ''.join(human_number).isalpha():
            print(INVALID_INPUT_WARNING)
            human_number = list(input(HUMAN_MESSAGE))
        elif len(set(human_number)) == len(human_number) == 4:
            input_check = False

    for digit in human_number:
        if digit in computer_number:
            if human_number.index(digit) == computer_number.index(digit):
                bulls += 1
            else:
                cows += 1

    print(f"{cows=}, {bulls=}")

    if human_number == computer_number:
        cowsay.cow("Well done! You've won!")
        break
