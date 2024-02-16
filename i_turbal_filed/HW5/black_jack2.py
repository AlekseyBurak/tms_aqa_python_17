import random

# создаем значения карты
cards = [str(i) for i in range(1, 11)] + ['J', 'Q', 'K', 'A']
# print(cards)
# create suit cards
suits = ("Diamonds", "Hearts", "Clubs", "Spades",)
all_cards = []
for card in cards:
    for suit in suits:
        all_cards.append(f"{card} - {suit}")
# print(all_cards)
# create scopes for cards

#mix cards:
for _ in range(5):
    random.shuffle(all_cards)
# print(all_cards)
# create scope for cards

scores = {}
for card in cards:
    if card.isdigit():
        scores[card] = int(card)
    elif card in "JQK":
        scores[card] = 10
    else:
        scores[card] = 11
# print(scores)

# создаем раздачу

dealer_hand = []
for _ in range(1):
    dealer_hand.append(all_cards.pop())
    dealer_hand.append(all_cards.pop(-1))
# print(dealer_hand)
#
# print(all_cards)

player_hand = []
for _ in range(1):
    player_hand.append(all_cards.pop())
    player_hand.append(all_cards.pop(-1))
# print(player_hand)
# print(all_cards)

# считаем очки полученные
dealer_score = 0
for card in dealer_hand:
    if card.startswith("10"):
        dealer_score += 10
    else:
        dealer_score += scores[card[0]]
print(dealer_hand)
print(dealer_score)

player_score = 0
for card in player_hand:
    if card.startswith("10"):
        player_score += 10
    else:
        player_score += scores[card[0]]
print(player_hand)
print(player_score)

question = input("Do you want to add card")
while True:
    if question == "yes":
        for _ in range(1):
            dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
        for card in dealer_hand:
            if card.startswith("10"):
                dealer_score += 10
            else:
                dealer_score += scores[card[0]]
        for _ in range(1):
            for _ in range(1):
                player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))
        print(dealer_hand)
        for card in player_hand:
            if card.startswith("10"):
                player_score += 10
            else:
                player_score += scores[card[0]]
        break
    elif question == "no":
        break





