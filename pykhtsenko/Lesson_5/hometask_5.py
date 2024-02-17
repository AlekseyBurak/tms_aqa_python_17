# программа для игры быки и коровы
import random
# компьютер генерирует рандомные числа
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digits[computer_player-1] = 0
for i in random.sample(digits,3):
    computer_player = computer_player*10+i


# пользователь вводит число
player = int(input())

# переводим числа в массив
player_list = list(str(player))
computer_player_list = list(str(computer_player))

#индексы для коров и быков
cow = []
bul = []

# сравниваем числа
for index in range(len(computer_player_list)):
    #если у игроки и у компьютера числа равны то это бык:
    if computer_player_list[index] == player_list[index]:
     bul.append(index)
     #если в числах есть одинаковые цифры, но на разных местах то это корова:
    elif computer_player_list[index] in player_list[]:
        cow.append((index))
