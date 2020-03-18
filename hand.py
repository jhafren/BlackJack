class Hand:

    def __init__(self, last_card_face_down = False):
        self.cards = []
        self.last_card_face_down = last_card_face_down

    def visible_cards(self):
        if self.last_card_face_down:
            return self.cards[:-1]

        return self.cards

    def simple_sum(self):
        '''
        Returns the BlackJack sums for the hand, 
        where aces are counted as 1.
        '''
        hand_sum = 0
        for card in self.visible_cards():
            hand_sum += card.black_jack_value()

        return hand_sum

    def hand_sums(self):
        '''
        Returns a list of the possible BlackJack sums for the hand, 
        taking into account that an ace can either be 1 or 11. 
        '''
        sums = [self.simple_sum()]

        for card in self.visible_cards():
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

    def draw_hand(self):
        '''
        Returns a string of cards in the hand, where the cards in
        the hand are drawn next to each other horisontally.
        '''
        drawn_card_rows = []
        for index, card in enumerate(self.cards):
            if self.last_card_face_down and index == len(self.cards)-1:
                drawn_card = card.draw_card_face_down()
            else:
                drawn_card = card.draw_card()
            drawn_card_rows.append(drawn_card.split("\n"))

        result = ""
        for row_ind in range(len(drawn_card_rows[0])):
            for card_ind in range(len(drawn_card_rows)):
                result += drawn_card_rows[card_ind][row_ind]

            result += "\n"

        return result

    def show_last_card(self):
        self.last_card_face_down = False

    def __str__(self):
        result = self.draw_hand()
        result += f"Sum {self.hand_sum()}"
        
        return result
