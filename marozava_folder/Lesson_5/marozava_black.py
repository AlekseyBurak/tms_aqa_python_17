
*не доделана задача, только то что на лекции

dealer_hand = []
player_hand = []

for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))

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
        dealer_score += scores[card[-1]]

print(f'{dealer_hand=} -- {dealer_score=}\n'
      f'{player_hand=} -- {player_score=}\n'
      f'{"Dealer win" if dealer_score >= player_score and dealer_score <= 21 else "Player win"}"')

*не доделана задача