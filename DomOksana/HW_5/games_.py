import random

#создаем карты
cards = [str(card) for card in range (2, 11)] + ['J', 'Q', 'K', 'A']
#print(cards)

#создаем масти
all_cards = list()
for c in cards:
   for suit in ("Diamonds", "Hearts", "Clubs", "Spades"):
     all_cards.append(f"{suit} - {c}")
# print(all_cards)
# print(len(all_cards))


#задаем цену карт
scores = dict()
for card in cards:
 if card.isdigit():
  scores[card] = int(card)
 elif card in 'JQK':
   scores[card] = 10
 elif card == 'A':
   scores[card] = 11
#print(scores)

#print(all_cards)
#перетасовываем карты
random.shuffle(all_cards)
print(all_cards)

#переменные для списка карт дилера и игрока
dealer_nand = []
player_hand = []
#выдаем по 2 случайные карты
for _ in range(2):
    dealer_nand.append(all_cards.pop(random.randrange(0, len(all_cards))))
for _ in range(2):
   player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
print(dealer_nand)
print(player_hand)

#считаем очки
dealer_score = 0
for card in dealer_nand:
    if card.endswith("10"):
        dealer_score +=10
    else:
        dealer_score += scores[card[-1]]
'''
если было 2 туза - второй туз считаем за 1 очко, т.е. 11-10=1
'''
if ''.join(dealer_nand).count('A') > 1:
    dealer_score -= 10

player_score = 0
for card in player_hand:
    if card.endswith("10"):
        player_score +=10
    else:
        player_score += scores[card[-1]]
if ''.join(player_hand).count('A') > 1:
    player_score -= 10

'''
предлагаем игроку выбор: 1 - добрать или  0 - остановиться
'''
print(f"у вас на руках {player_hand=}, ваши очки {player_score=} ")
v = int(input("сделайте выбор: 1 - добрать или  0 - остановиться: "))
print(v)
if v == 0:
    print(f"{dealer_nand=} -- {dealer_score=}\n"
      f"{player_hand=} -- {player_score=}\n"
      f"{'Вы проиграли :(' if dealer_score >= player_score and dealer_score <= 21 else 'Вы выиграли'}")
elif v == 1:
    # выдаем 1 карту
    player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
    #считаем очки
    player_score = 0
    for card in player_hand:
        if card.endswith("10"):
            player_score += 10
        else:
            player_score += scores[card[-1]]
    if ''.join(player_hand).count('A') > 1:
        player_score -= 10
    print(f"у вас на руках {player_hand=}, ваши очки {player_score=} ")
    print(f"{dealer_nand=} -- {dealer_score=}\n"
          #f"{player_hand=} -- {player_score=}\n"
          f"{'Вы проиграли :(' if (dealer_score >= player_score and dealer_score <= 21) 
                                  or player_score >21 else 'Вы выиграли'}")
else:
    print("Вы ошиблись командой, игра прервана")