from random import triangular
from .Panel import Panel
from .Storage import Storage
from .Villager import Villager
from .Business import Business
from .functions import scaled_gaussian


class Central:
    def __init__(self, token_per_kw, nb_villagers):
        self.panels = []
        self.storages = []
        self.cash = []
        self.villagers = []
        self.businesses = []
        self.hospital_consumption = 0
        self.token_per_kW = token_per_kw
        self.nb_villagers = nb_villagers
        self.step_production = 0
        self.m_step_production = 0
        self.time = 7
        self.init_villagers()

    def init_villagers(self):
        for i in range(self.nb_villagers):
            self.add_villager()

    def add_panel(self):
        self.panels.append(Panel())

    def add_storage(self):
        self.storages.append(Storage())

    def add_villager(self):
        villager = Villager(triangular(0, 1), triangular(0, 1))
        self.villagers.append(villager)

    def add_business(self):
        self.businesses.append(Business())

    def step(self):
        self.step_production = 0
        self.m_step_production = 0
        self.produce()
        self.consume()
        self.store()
        self.time += 1

    def produce(self):
        for panel in self.panels:
            self.step_production += panel.produce(self.time)
        self.m_step_production = self.step_production

    def consume(self):
        # Compute consumption

        # Update hospital consumption
        self.hospital_cons()

        # Update villagers needed consumption
        for v in self.villagers:
            v.needed_consumption_update(self.time)

        # Update businesses needed consumption
        for b in self.businesses:
            b.needed_consumption_update(self.time)

        pass

    def store(self):
        for storage in self.storages:
            if self.step_production:
                self.step_production = storage.fill(self.step_production)
            else:
                break
        self.distribute_tokens((self.m_step_production - self.step_production) / self.token_per_kW)

    def distribute_tokens(self, quantity):
        # Give N tokens to each villager
        pass

    def hospital_cons(self):
        t = self.time % 24
        offset = 2
        scale = 3
        mu = 13
        var = 4**2
        self.hospital_consumption = offset + scale*scaled_gaussian(mu, var, t)
