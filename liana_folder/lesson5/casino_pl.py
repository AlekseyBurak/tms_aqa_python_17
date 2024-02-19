import random

cards = [str(card) for card in range(2, 11)] + ['J', 'Q', 'K', 'A']

all_cards = list()
for i in cards:
    for suit in ('Diamonds', 'Hurts', 'Clubs', 'Spiders'):
        all_cards.append(f"{suit} - {i}")

for _ in range(5):
    random.shuffle(all_cards)

scores = dict()

for card in cards:
    if card.isdigit():
        scores[card] = int(card)
    elif card in 'JQK':
        scores[card] = 10
    elif card == 'A':
        scores[card] = 11

dealer_hand = []
player_hand = []

for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(cards))))

for _ in range(2):
    player_hand.append(all_cards.pop(random.randrange(0, len(cards))))

dealer_score = 0
for card in dealer_hand:
    if card.endswith("10"):
        dealer_score += 10
    else:
        dealer_score += scores[card[-1]]

player_score = 0
for card in player_hand:
    if card.endswith("10"):
        player_score += 10
    else:
        player_score += scores[card[-1]]

print(f"{dealer_hand=} -- {dealer_score}\n"
      f"{player_hand=} -- {player_score}\n")

print("WINNER")
if dealer_score >= player_score <= 21:
    print("Dealer win!")
else:
    print("Player win!")
