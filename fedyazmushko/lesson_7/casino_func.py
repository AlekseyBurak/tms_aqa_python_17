import random

cards = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

def create_card_deck():
    all_cards = [f'{d} - {i}' for i in cards for d in ('Diamonds', 'Hearts', 'Clubs', 'Spades')]
    return all_cards


def shuffle_deck(deck):
    for _ in range(5):
        random.shuffle(deck)
    return deck


def create_scores():
    scores = {}
    for i in cards:
        if i.isdigit():
            scores[i] = int(i)
        elif i in "JQK":
            scores[i] = 10
        elif i == 'A':
            scores[i] = 11
    return scores


def deal_cards(deck):
    hand = []
    for _ in range(2):
        hand.append(deck.pop(random.randrange(0, len(deck))))
    return hand


def calculate_score(hand, scores):
    score = 0
    for card in hand:
        value = card.split(' - ')[1]
        score += scores[value]
    return score


def play_blackjack():
    deck = create_card_deck()
    shuffled_deck = shuffle_deck(deck)

    scores = create_scores()

    dealer_hand = deal_cards(shuffled_deck)
    player_hand = deal_cards(shuffled_deck)

    dealer_score = calculate_score(dealer_hand, scores)
    player_score = calculate_score(player_hand, scores)

    print(f'Dealer hand: {dealer_hand} -- {dealer_score}')
    print(f'Player hand: {player_hand} -- {player_score}')
    print("Dealer wins" if dealer_score >= player_score and dealer_score <= 21 else "Player wins")


play_blackjack()