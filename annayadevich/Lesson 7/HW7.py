
#Игра "Быки и коровы"
import random
def generate_secret_number():
    """Генерирует случайное 4-значное число с неповторяющимися цифрами."""
    secret_number = ''.join(random.sample('0123456789', 4))
    print(f"Generated number: {secret_number}")
    return secret_number

def count_bulls_and_cows(secret, my_num):
    """Определяет количество быков и коров."""
    bulls, cows = 0, 0
    for i in range(4):
        if secret[i] == my_num[i]:
            bulls += 1
        elif secret[i] in my_num:
            cows += 1
    return bulls, cows

def main():
    print("Welcome to the game 'Bulls and Cows'!")
    secret_number = generate_secret_number()
    attempts = 0

    while True:
        my_num = input("Enter your number: ")
        if not my_num.isdigit() or len(my_num) != 4 or len(set(my_num)) != 4:
            print("Incorrect input. Try again.")
            continue

        bulls, cows = count_bulls_and_cows(secret_number, my_num)
        attempts += 1

        if bulls == 4:
            print(f"You've won! The hidden number was {secret_number}.")
            print(f"Number of attempts: {attempts}")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")
main()

#Про урок физкультуры задача
def sorted_height():
    all_height_from_class = [165, 163, 162, 160, 157, 157, 155, 154]
    petya_height = 162
    index_to_insert = all_height_from_class.index(petya_height) + 1
    all_height_from_class.insert(index_to_insert, petya_height)
    print(all_height_from_class)

sorted_height()
