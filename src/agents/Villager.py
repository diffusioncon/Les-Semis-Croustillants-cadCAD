from numpy import pi, exp
from .Market import Market

CONS_OFFSET = 0.2
MORNING_SCALE = 0.4
EVENING_SCALE = 0.8


class Villager:
    market = Market()

    def __init__(self):
        self.bank = 0
        self.needed_consumption = 0
        self.consumption = 0
        self.tokens = set()
        self.tokens_on_market = set()

    def credit(self, price):
        self.bank += price

    def debit(self, price):
        self.bank -= price

    def add_token(self, token):
        token.owner = self
        self.tokens.add(token)

    def remove_token(self, token):
        self.tokens_on_market.remove(token)

    def sell(self, token):
        self.tokens.remove(token)
        if not Villager.market.ask(token):
            self.tokens_on_market.add(token)

    def buy(self, quantity):
        Villager.market.bid(self, quantity)

    def needed_consumption_update(self, time):
        t = time % 24
        self.needed_consumption = CONS_OFFSET + MORNING_SCALE*self.gaussian(7, 1.25**2, t) + EVENING_SCALE*self.gaussian(20, 2.5**2, t)

    def gaussian(self, mu, var, x):
        return 1/(2*pi*var)*exp(-(x-mu)**2/2/var)
