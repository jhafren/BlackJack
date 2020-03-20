class Bankroll:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insuffiient funds")

        self.balance -= amount

    def has_balance(self):
        return self.balance > 0

    def __str__(self):
        return f"Bankroll balance {self.balance}"