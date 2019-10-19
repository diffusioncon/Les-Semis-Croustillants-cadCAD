from random import triangular
from .Panel import Panel
from .Storage import Storage
from .Villager import Villager
from .Business import Business
from .Token import Token
from numpy import pi, exp


class Central:
    def __init__(self, token_per_kw, nb_villagers):
        self.panels = []
        self.storages = []
        self.cash = []
        self.villagers = []
        self.businesses = []
        self.token_per_kW = token_per_kw
        self.nb_villagers = nb_villagers
        self.step_production = 0
        self.m_step_production = 0
        self.time = 7
        self.current_token_id = 0
        self.init_simulation()

    def init_simulation(self):
        for i in range(self.nb_villagers):
            self.add_villager()
        for i in range(self.nb_villagers / 100):
            self.add_business()

    def step(self):
        self.step_production = 0
        self.m_step_production = 0
        self.produce()
        self.hospital_consumption()
        self.distribute_tokens()
        self.compute_needed_consumption()
        self.trade()
        self.consume()
        self.store()
        self.time += 1

    def distribute_tokens(self):
        quantity = self.step_production / self.token_per_kW
        for _ in range(quantity):
            villager = self.villagers[self.current_token_id]
            villager.add_token(Token())
            if self.current_token_id == self.nb_villagers - 1:
                self.current_token_id = 0
            else:
                self.current_token_id += 1

    def add_panel(self):
        self.panels.append(Panel())

    def add_storage(self):
        self.storages.append(Storage())

    def add_villager(self):
        villager = Villager(triangular(0, 1), triangular(0, 1))
        self.villagers.append(villager)

    def add_business(self):
        self.businesses.append(Business(triangular(0, 0.5), triangular(1, 2)))

    def produce(self):
        for panel in self.panels:
            self.step_production += panel.produce(self.time)
        self.m_step_production = self.step_production

    def compute_needed_consumption(self):
        for v in self.villagers:
            v.needed_consumption_update(self.time)
        for b in self.businesses:
            b.needed_consumption_update(self.time)

    def trade(self):
        pass

    def consume(self):
        pass

    def store(self):
        for storage in self.storages:
            if not self.step_production:
                return
            self.step_production = storage.fill(self.step_production)

    def take_from_storage(self, quantity):
        for storage in self.storages:
            quantity = storage.take(quantity)
            if quantity == 0:
                return quantity
        return quantity

    def hospital_consumption(self):
        t = self.time % 24
        offset = 2
        scale = 3
        mu = 13
        var = 4 ** 2
        hospital_consumption = offset + scale * 1 / (2 * pi * var) * exp(-(t - mu) ** 2 / 2 / var)
        delta = self.step_production - hospital_consumption
        if delta > 0:
            self.step_production -= hospital_consumption
        else:
            self.step_production = 0
            if self.take_from_storage(-delta) > 0:
                print("WE DONT HAVE ENOUGH ELECTRICITY FOR THE HOSPITAL!")
