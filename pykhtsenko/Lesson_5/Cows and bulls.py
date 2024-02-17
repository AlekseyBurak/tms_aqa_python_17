
# генерация числа компьютером
import random
computer_player = random.sample("123456789",4)
#print(f"Генерируемое число компьютером было: ", int("".join(computer_player)))
# пользователь вводит число
player = int(input("Введите 4ех значное число, без повторяющихся чисел: "))
# находим количество быков и коров
cows = 0
bulls = 0
# переводим числа в массив
player_list = list(str(player))
if len(player_list) > 4:
    print(" Ошибка!Больше чем 4 символа!")
else:
    for idx1, elem1 in enumerate(player_list):
        for idx2, elem2 in enumerate(computer_player):
            if (elem2 == elem1):
                if (idx1 == idx2):
                    bulls +=1
                else:
                    cows +=1
#while computer_player != player:
    #player = int(input("Введите 4ех значное число, без повторяющихся чисел: "))
#else:
    #print(f"Генерируемое число компьютером было: ", int("".join(computer_player)))
print(f"cows: {cows}")
print(f"bulls: {bulls}")
print(f"Генерируемое число компьютером было: ", int("".join(computer_player)))
