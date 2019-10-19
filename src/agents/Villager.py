class Villager:
    def __init__(self):
        self.bank = 0
        self.consumption = 0
        self.tokens = set()

    def credit(self, price):
        self.bank += price

    def debit(self, price):
        self.bank -= price

    def add_token(self, token):
        self.tokens.add(token)

    def remove_token(self, token):
        self.tokens.remove(token)

