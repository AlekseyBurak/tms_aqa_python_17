# Суть: Я раздаю диллеру и игроку по две карту, одну ссверху и одну снизу, что не имеет значение
# Карты диллера не показываю
# После создаю цикл while True (так нельзя, но я не придумал как по другому :))
# если на вопрос ответ yes, то добавляется карта диллеру и игроку, обнуляется пред. очки и считаются заново.
# если ответ !yes, то выходим с цикла
# после сверяем результаты
# про тузы когда после 21 не делал, возможно к этому вопросу вернусть позже

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


while True:
    question = input("Do you want to add card")
    # добавляем карту диллеру
    if question == "yes":
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
    elif question == "no":
        break



# проверка результата
if player_score > 21 and dealer_score > 21:
    if player_score < dealer_score:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")
    elif player_hand > dealer_hand:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")
    elif player_hand == dealer_hand:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You and dealer has the same points!")
if player_score < 21 and dealer_score < 21:
    if player_score < dealer_score:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")
    elif player_hand > dealer_hand:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")
    elif player_hand == dealer_hand:
        print(f" You have {player_score}\n delaer has {dealer_score}\n You and dealer has the same points!")
if player_score < 21 and dealer_score > 21:
    print(f" You have {player_score}\n delaer has {dealer_score}\n You win!")
if player_score > 21 and dealer_score < 21:
    print(f" You have {player_score}\n delaer has {dealer_score}\n You lose!")


