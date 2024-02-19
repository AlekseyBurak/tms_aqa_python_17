import random

"""
Мы создаем список в котором будут значания карт. Для этого мы создаем с помощью list comprehension список цифр от 2 до 10
и прибавляем к нему список со значиниями для карт с картинками
"""
cards = [str(card) for card in range(2, 11)] + ['J', 'Q', 'K', 'A']
"""
с помощью первого цикла for мы итерируемся по списку со значениями карт.
с помощью второго цикла for мы берем каждое отдельное значение, добавляем к нему масть, добавляем получившуюся карту в заранее созданный список
"""
all_cards = list()
for c in cards:
    for suit in ("Diamonds", "Hearts", "Clubs", "Spades"):
        all_cards.append(f"{suit} - {c}")

"""
С помощью функции random.shuffle мы перемешиваем элементы списка, в котором лежат все наши карты (масть -- значание)
"""
for _ in range(5):
    random.shuffle(all_cards)

scores = dict()

"""
Создаем пустой словарь в котором буем хранить количество очков для каждой карты. В подсчете очков нас не интересует масть.
Поэтому мы используем самый первый список, список значений карт. Из него мы возьмем ключи для словаря.
"""
for card in cards:  # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    if card.isdigit():
        scores[card] = int(card)
    elif card in 'JQK':
        scores[card] = 10
    elif card == 'A':
        scores[card] = 11

"""
создаем два пустых списка. туда будем складывать карты для игрока и диллера.
"""
dealer_hand = []
player_hand = []

"""
метод pop удалит элемент из списка и вернет его нам. 
если не задавать индекс элемента, рор удалит и вернет нам последний элемент.
мы используем random.randrange чтобы найти случайное число в диапазоне от 0 до длинны списка карт. 
Мы не можем установить диапазон от 0 до 52 потому что правую граицу нужно пересчитывать после каждого удаления карты из списка-колоды
"""
for _ in range(2):
    dealer_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))

for _ in range(2):
    player_hand.append(all_cards.pop(random.randrange(0, len(all_cards))))

"""
Начинем предварительный подсчет очков.

"""
dealer_score = 0

for card in dealer_hand:
    if card.endswith("10"):
        dealer_score += 10
        # здесь мы проверяем, нет ли у нас карты со значением 10. Если есть - добавляем 10 очков.
    else:
        dealer_score += scores[card[-1]]
        # здесь происходит обращение к словарю с очками для карт. предположим что с переменной cart 'Diamonds - K'.
        # это строка. берем ее срез как в коде выше. получается 'K'. 'K' в свою очередь это ключ словаря. со значением 10
        # поэтому строка выше преобразвется в выражение dealer_score = dealer_score + 10

'''
Здесь я проверяю, нет ли у нас второго туза в руке. если он есть, сумма очков будет уменьшена на 10, чтобы не допустить перебора.

Вот что выдал мне GPT

В блэкджеке, если у игрока есть туз, то он может считать его как 1 или как 11 очков в зависимости от ситуации. 
Если после добавления туза к сумме карт у игрока сумма превышает 21, то туз считается за 1 очко. 
Если же сумма не превышает 21, то туз может быть посчитан за 11 очков для получения наилучшей комбинации карт.

Если у игрока в руке два туза, то один из них обычно считается за 11 очков, а другой за 1 очко. 
Таким образом, сумма очков будет равна 12. Это позволяет избежать превышения суммы 21, 
так как если бы оба туза считались за 11 очков, то сумма была бы равна 22, что приводит к проигрышу.
'''
if ''.join(dealer_hand).count('A') > 1:
    dealer_score -= 10

'''
все то же самое но для руки игрока
'''
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
    '''
    Выводим руку игрока. Предлагаем ему добрать еще карту или закончить играть
    повторяем код для добавления карт.
    повторяем код для подсчета очков.
    все это в бесконечном цикле while. Точки выхода две:
    1) либо игрок выходит сам. 
    2) либо у него перебор

    '''
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
