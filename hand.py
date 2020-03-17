class Hand:

    def __init__(self):
        self.cards = []

    def simple_sum(self):
        '''
        Returns the BlackJack sums for the hand, 
        where aces are counted as 1.
        '''
        hand_sum = 0
        for card in self.cards:
            hand_sum += card.black_jack_value()

        return hand_sum

    def hand_sums(self):
        '''
        Returns a list of the possible BlackJack sums for the hand, 
        taking into account that an ace can either be 1 or 11. 
        '''
        sums = [self.simple_sum()]

        for card in self.cards:
            if card.is_ace():
                sums.append(sums[-1] + 10)

        return sums

    def hand_sum(self):
        '''
        Returns the highest possible sum of the hand that is not bust (<=21),
        or the lowest busted sum
        '''
        for hand_sum in self.hand_sums()[::-1]:
            if hand_sum <= 21:
                return hand_sum
        
        return hand_sum


    def take(self, card):
        self.cards.append(card)

    def __str__(self):
        result = ""
        for card in self.cards:
            result += f"{card}\n"

        result += f"Sum {self.hand_sum()}"
        
        return result
