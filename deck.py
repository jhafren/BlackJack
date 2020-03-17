from random import shuffle
from card import Card

class Deck:

    suits = ["hearts", "diamonds", "clubs", "spades"]

    def __init__(self):
        self.cards = []

        for suit in Deck.suits:
            for rank in range(1, 14):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        shuffle(self.cards)

    def draw_card(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            print("Deck is empty")
            return None
