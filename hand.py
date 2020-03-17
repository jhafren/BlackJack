class Hand:

    def __init__(self):
        self.cards = []

    def sum(self):
        sum = 0
        for card in self.cards:
            sum += card.black_jack_value()

        return sum

    def take(self, card):
        self.cards.append(card)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += f"{card}\n"

        result += f"Sum {self.sum()}"
        
        return result
