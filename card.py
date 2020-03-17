class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

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
