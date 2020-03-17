class Hand:

    def __init__(self):
        self.cards = []

    '''
    Returns the BlackJack sums for the hand, 
    where aces are counted as 1. 
    '''
    def simple_sum(self):
        sum = 0
        for card in self.cards:
            sum += card.black_jack_value()

        return sum

    '''
    Returns a list of the possible BlackJack sums for the hand, 
    taking into account that an ace can either be 1 or 11. 
    '''
    def sums(self):
        
        sums = [self.simple_sum()]

        for card in self.cards:
            if card.is_ace():
                sums.append(sums[-1] + 10)

        return sums

    '''
    Returns the highest possible sum of the hand that is not bust (<=21),
    or the lowest busted sum
    '''
    def sum(self):
        for sum in self.sums()[::-1]:
            if sum <= 21:
                return sum
        else:
            return sum


    def take(self, card):
        self.cards.append(card)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += f"{card}\n"

        result += f"Sum {self.sum()}"
        
        return result
