# Суть: Я раздаю диллеру и игроку по две карту, одну ссверху и одну снизу, что не имеет значение
# После создаю цикл while True

import random

# создаем значения карты
cards = [str(i) for i in range(1, 11)] + ['J', 'Q', 'K', 'A']
suits = ("Diamonds", "Hearts", "Clubs", "Spades",)
all_cards = []
for card in cards:
    for suit in suits:
        all_cards.append(f"{card} - {suit}")

#mix cards:
for _ in range(5):
    random.shuffle(all_cards)
# create scope for cards

scores = {}
for card in cards:
    if card.isdigit():
        scores[card] = int(card)
    elif card in "JQK":
        scores[card] = 10
    else:
        scores[card] = 11

# создаем раздачу

dealer_hand = []
for _ in range(1):
    dealer_hand.append(all_cards.pop())
    dealer_hand.append(all_cards.pop(-1))


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


player_score = 0
for card in player_hand:
    if card.startswith("10"):
        player_score += 10
    else:
        player_score += scores[card[0]]
print(f"Your cards is {player_hand}\n and your scope is {player_score}")

print(scores)
while True:
    question = input("Do you want to add card? enter any value enter any value other than yes if no ").lower()
    # добавляем карту диллеру
    if question == "yes" or question == "y" or question ==  "+":
        for _ in range(1):
            dealer_hand.append(all_cards.pop(-1))
        dealer_score = 0
        for card in dealer_hand:
            if card.startswith("10"):
                dealer_score += 10
            else:
                dealer_score += scores[card[0]]
        for _ in range(1):
            for _ in range(1):
                player_hand.append(all_cards.pop(-1))
        player_score = 0
        for card in player_hand:
            if card.startswith("10"):
                player_score += 10
            else:
                player_score += scores[card[0]]
        print(f"Your cards is {player_hand}\n and your scope is {player_score}")
    else:
        break

print(f"your score {player_score} and your cards {player_hand} ")
print(f"dealer's score {dealer_score} and dealer cards {dealer_hand}")
print("-"*15 + "Results" + "-" * 15)


#блок проверки если у обоих больше 21 - работает все верно
if (player_score >= 21 and dealer_score > 21) or (player_score > 21 and dealer_score >= 21): # work
    if player_score == dealer_score: #work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You and dealer has the same points!")
    elif player_score > dealer_score: #work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")
    elif player_score < dealer_score:# work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")


#блок если у обоих меньше 21 - работает все верно
elif (player_score <= 21 and dealer_score < 21) or (player_score < 21 and dealer_score <= 21) : # work
    if player_score == dealer_score: #work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You and dealer has the same points!")
    elif player_score > dealer_score: #work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")
    elif player_score < dealer_score:# work
        print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")

# блок если у обоих 21
elif player_score == 21 and dealer_score == 21: # work
    print(f" You have {player_score}\n delaer has {dealer_score}\n You and dealer has the same points!")
elif player_score > 21 and dealer_score <= 21:
    print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")
elif player_score <= 21 and dealer_score > 21: # work
    print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")






# 16 11 - the same 14 16 17 8 - lose - сравнения
# 15 18 - win 17 13 - nothing 18 10 - nothing 19 - 7