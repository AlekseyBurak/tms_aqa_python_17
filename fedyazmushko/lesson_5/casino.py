import random

cards = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

all_cards = list()

for i in cards:
    for d in ('Diamonds', 'Hearts', 'Clubs', 'Spades'):
        all_cards.append(f'{d} - {i}')

print(all_cards)
for _ in range(5):
    random.shuffle(all_cards)

print(all_cards)

scores = dict()

for i in cards:
    if i.isdigit():
        scores[i] = int(i)
    elif i in "JQK":
        scores[i] = 10
    elif i == 'A':
        scores[i] = 11

dealer_hand = []
player_hand = []

for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
    player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))

dealer_scores = 0

for i in dealer_hand:
    if i.endswith('10'):
        dealer_scores += 10
    else:
        dealer_scores += scores[i[-1]]

player_score = 0

for i in player_hand:
    if i.endswith('10'):
        player_score += 10
    else:
        player_score += scores[i[-1]]

print(f'{dealer_hand=} -- {dealer_scores}\n'
      f'{player_hand} -- {player_score}\n'
      f"{'Dealer win' if dealer_scores >= player_score and dealer_scores <= 21 else 'Player win'}")






