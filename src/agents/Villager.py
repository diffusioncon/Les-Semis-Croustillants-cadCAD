from numpy import pi, exp

CONS_OFFSET = 0.2
MORNING_SCALE = 0.4
EVENING_SCALE = 0.8

class Villager:
    def __init__(self):
        self.bank = 0
        self.needed_consumption = 0
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

    def needed_consumption_update(self, time, offset=CONS_OFFSET, morning_scale=MORNING_SCALE, evening_scale=EVENING_SCALE):
        t = time % 24
        self.needed_consumption = offset + morning_scale*self.gaussian(7, 1.25**2, t) + evening_scale*self.gaussian(20, 2.5**2, t)

    def gaussian(self, mu, var, x):
        return 1/(2*pi*var)*exp(-(x-mu)**2/2/var)