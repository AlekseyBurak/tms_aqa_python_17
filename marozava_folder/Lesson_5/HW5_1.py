# 1) Быки и коровы
# В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает и записывает тайное 4-значное число
# с неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает первую попытку отгадать число. Попытка — это 4-значное
# число с неповторяющимися цифрами, сообщаемое противнику. Противник сообщает в ответ, сколько цифр угадано без совпадения
# с их позициями в тайном числе (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
# Пример
# Загадано число 3219
# >>> 2310
# Две коровы, один бык
# >>> 3219

import random

digits = list(range(10))
number_as_list = random.sample(digits, 4)
#print(number_as_list)

while True:
    player_number = input('Enter yor number: ')

    if len(player_number) != 4 or not player_number.isdigit() or len(set(player_number)) != 4:
        print('You entered wrong number!')
        continue
    if int(player_number) == int(''.join(map(str, number_as_list))):
        print('You guessed correct number!')
        break

    cow = 0
    bull = 0
    for i in range(4):
        digit = int(player_number[i])
        if digit in number_as_list:
            if number_as_list[i] == digit:
                bull = bull + 1
            else:
                cow = cow + 1
    print(f'Bull {bull}, Cow {cow} ')






