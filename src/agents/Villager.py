from math import ceil
from .Constants import KWH_PER_TOKEN
from .Market import Market
from .functions import scaled_gaussian


NO_ENERGY_FEE = 1


class Villager:
    market = Market()

    def __init__(self, morning_scale, evening_scale):
        self.morning_scale = morning_scale
        self.evening_scale = evening_scale
        self.employed = False
        self.bank = 10000
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
        self.tokens_on_market.add(token)
        Villager.market.ask(token)

    def buy(self, quantity):
        Villager.market.bid(self, quantity)

    def pull_from_market(self, quantity):
        for _ in range(quantity):
            token = self.tokens_on_market.pop()
            token.remove_from_market()
            Villager.market.pull_from_ask(token)
            self.tokens.add(token)

    def needed_consumption_update(self, time):
        t = time % 24
        minimum_consumption = .2
        self.needed_consumption = minimum_consumption + self.morning_scale * \
                                  scaled_gaussian(7, 1.25 ** 2, t) + self.evening_scale * \
                                  scaled_gaussian(20, 2.5 ** 2, t)

    def trade(self):
        tokens_quantity = len(self.tokens)
        available_consumption = tokens_quantity * KWH_PER_TOKEN
        if self.needed_consumption > available_consumption:
            missing_tokens = (self.needed_consumption - available_consumption) / KWH_PER_TOKEN
            on_market_count = len(self.tokens_on_market)
            if on_market_count > missing_tokens:
                to_pull = on_market_count - missing_tokens
            else:
                to_pull = on_market_count
            self.pull_from_market(int(to_pull))
            missing_tokens -= on_market_count
            if missing_tokens:
                self.buy(ceil(missing_tokens))
        else:
            excess = (available_consumption - 10 * self.needed_consumption) / KWH_PER_TOKEN
            if excess > 0:
                for i in range(int(excess)):
                    token = tuple(self.tokens)[0]
                    self.sell(token)

    def not_enough_energy(self):
        self.bank -= NO_ENERGY_FEE

    def consume(self):
        tokens_needed = ceil(self.needed_consumption / KWH_PER_TOKEN)
        for _ in range(tokens_needed):
            if len(self.tokens):
                self.tokens.pop()
            else:
                self.not_enough_energy()
                return

    def __lt__(self, other):
        return self.bank < other.bank
