from numpy import pi, exp
from .Market import Market

CONS_OFFSET = 0.2


class Villager:
    market = Market()

    def __init__(self, morning_scale, evening_scale):
        self.morning_scale = morning_scale
        self.evening_scale = evening_scale
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

    def needed_consumption_update(self, time, offset=CONS_OFFSET):
        t = time % 24
        self.needed_consumption = offset + self.morning_scale*self.gaussian(7, 1.25**2, t) + self.evening_scale*self.gaussian(20, 2.5**2, t)

    def gaussian(self, mu, var, x):
        return 1/(2*pi*var)*exp(-(x-mu)**2/2/var)
