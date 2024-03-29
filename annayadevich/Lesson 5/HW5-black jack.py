import random

cards = [str(card) for card in range(2, 11)] +['J', 'Q', 'K', 'A']
all_cards = list()
for c in cards:
    for suit in ('Diamonds', 'Hearts', 'Clubs', 'Spades'):
        all_cards.append(f"{suit} - {c}")

#print(all_cards)
for _ in range(5):
    random.shuffle(all_cards)
#print(all_cards)

scores = dict()

for card in cards:
     if card.isdigit():
         scores[card] = int(card)
     elif card in 'JQK':
         scores[card] = 10
     elif card == 'A':
         scores[card] = 11

#print()
#print(scores)

dealer_hand = []
player_hand = []

for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))

for _ in range(2):
    player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))


dealer_score = 0

for card in dealer_hand:
    if card.endswith("10"):
        dealer_score += 10

    else:
        dealer_score += scores[card[-1]]


if ''.join(dealer_hand).count('A') > 1:
    dealer_score -= 10

player_score = 0

for card in player_hand:
    if card.endswith("10"):
        player_score += 10
    else:
        player_score += scores[card[-1]]

if ''.join(player_hand).count('A') > 1:
    player_score -= 10

game_result = "Spare"

while True:

    print(f"Your hand -- {player_hand=} -- score -- {player_score}")
    command = input("Hit '1' if you want more cards\n"
                    "Hit '2' if you want to stop\n")
    if command == "2":
        break
    elif command == "1":
        one_more_card = all_cards.pop(random.randrange(0, len(all_cards)))
        if one_more_card.endswith("A"):
            if player_score > 10:
                player_score += 1
            else:
                player_score += 11

        elif one_more_card.endswith("10"):
            player_score += 10
        else:
            player_score += scores[one_more_card[-1]]
        player_hand.append(one_more_card)
        if player_score >= 21:
            break
    else:
        print("Введите правильную команду")

if player_score <= dealer_score <= 21:
    game_result = 'Dealer win'
elif dealer_score < player_score <= 21:
    game_result = 'Player win'
elif dealer_score > 21 >= player_score:
    game_result = 'Player win'
elif player_score > 21 >= dealer_score:
    game_result = 'Dealer win'

print(f"{dealer_hand=} -- {dealer_score=}\n"
      f"{player_hand=} -- {player_score=}\n"
      f"{game_result}")
