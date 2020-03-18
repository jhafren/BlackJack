class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def rank_char(self):
        if self.rank == 1:
            return "A"
        if self.rank == 11:
            return "J"
        if self.rank == 12:
            return "Q"
        if self.rank == 13:
            return "K"
        return f"{self.rank}"

    def suit_char(self):
        if self.suit =="hearts":
            return "♥" 
        if self.suit == "diamonds":
            return "♦"
        if self.suit == "clubs":
            return "♣"
        return "♠"

    def draw_card(self):
        '''
        Returns a string with the face of the card drawn, e.g.:
         _ _ _
        |A    |
        |♣    |
        |    ♣|
        |    A|
         ̅  ̅  ̅ 
        '''
        return (" _ _ _  \n" +
            f"|{self.rank_char():<2}   | \n" +
            f"|{self.suit_char()}    | \n" +
            f"|    {self.suit_char()}| \n" +
            f"|   {self.rank_char():>2}| \n" +
            " ̅ ̅ ̅  ")

    def draw_card_face_down(self):
        '''
        Returns a string with the of the card drawn face down
        '''
        return (" _ _ _  \n" +
            "|XXXXX| \n" +
            "|XXXXX| \n" +
            "|XXXXX| \n" +
            "|XXXXX| \n" +
            " ̅ ̅ ̅  ")

    def __str__(self):   
        rank_str = self.rank

        if self.rank == 1:
            rank_str = "ace"
        elif self.rank == 11:
            rank_str = "jack"
        elif self.rank == 12:
            rank_str = "queen"
        elif self.rank == 13:
            rank_str = "king"

        return f"{rank_str} of {self.suit}"

    def black_jack_value(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank

    def is_ace(self):
        return self.rank == 1
