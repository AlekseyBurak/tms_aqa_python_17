import random
# функция получения перетасованной калоды
def karty ():
    cards = [str(card) for card in range (2, 11)] + ['J', 'Q', 'K', 'A']
    all_cards = list()
    for c in cards:
        for suit in ("Diamonds", "Hearts", "Clubs", "Spades"):
            all_cards.append(f"{suit} - {c}")
    random.shuffle(all_cards)
    return all_cards

#функция получения справочника очков
def ochky():
    scores = dict()
    for card in [str(card) for card in range(2, 11)] + ['J', 'Q', 'K', 'A']:
        if card.isdigit():
            scores[card] = int(card)
        elif card in 'JQK':
            scores[card] = 10
        elif card == 'A':
            scores[card] = 11
    return scores

#функция раздачи карт
def razdacha (k, koloda_x):
    razd = []
    for _ in range(k):
        razd.append(koloda_x.pop(random.randrange(0, len(koloda_x))))
    return razd

#функция подсчета карт на руках
def schet(o_sprav,k_igroka):
    schet_x = 0
    for c in k_igroka:
        if c.endswith("10"):
            schet_x += 10
        else:
            schet_x += o_sprav[c[-1]]
    if ''.join(k_igroka).count('A') > 1:
        schet_x -= 10
    return schet_x

#функция выбора варианта действий
def variant(my_och, koloda_y, s_och):
    game_res = False
    while game_res != True:
        print(f"У вас очков: {my_och}")
        #print(f"Ваши карты {player_hand} , у вас очков: {player_score}")
        com = input("Введите\n"
                    f" 1 чтобы добрать карту или\n"
                    f" 2 чтобы открыть карты: ")
        if com == "2":
            break
        elif com == "1":
            nov_card = koloda_y.pop(random.randrange(0, len(koloda_y)))
            if nov_card.endswith("A"):
                if my_och > 10:
                    my_och += 1
                else:
                    my_och += 11
            elif nov_card.endswith("10"):
                my_och += 10
            else:
                my_och += s_och[nov_card[-1]]
            player_hand.append(nov_card)
            if my_och >= 21:
                break
        else:
            print("Введите правильную команду: ")
    return my_och



# ИГРАЕМ
#получаем калоду перетасованых карт
koloda = karty()
print(koloda)
#создаем справочник очков
och = ochky()
print(och)
#раздаем по 2 карты
dealer_hand = razdacha(2, koloda)
player_hand = razdacha(2, koloda)

print(dealer_hand)
print(player_hand)

#считаем карты на руках
dealer_score = schet(och, dealer_hand)
player_score = schet(och, player_hand)

#предлагаем вариант добрать или остановиться
player_score = variant(player_score, koloda, och)


if player_score <= dealer_score <= 21:
    game_result = 'Вы проиграли'
elif dealer_score < player_score <= 21:
            game_result = 'Вы выиграли'
elif dealer_score > 21 >= player_score:
            game_result = 'Вы выиграли'
elif player_score > 21 >= dealer_score:
            game_result = 'Вы проиграли'

print(f"Карты диллера {dealer_hand}, у него очков: {dealer_score}\n"
      f"Ваши карты {player_hand}, ваши очки {player_score}\n"
      f"{game_result}")

