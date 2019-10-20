from random import triangular, shuffle, randint
import time
from .Panel import Panel
from .Storage import Storage
from .Villager import Villager
from .Business import Business
from .Token import Token
from .functions import scaled_gaussian


class Central:
    def __init__(self, nb_villagers):
        self.panels = []
        self.storages = []
        self.cash = []
        self.villagers = []
        self.businesses = []
        self.nb_villagers = nb_villagers
        self.step_production = 0
        self.m_step_production = 0
        self.time = 7
        self.current_token_id = 0
        self.init_simulation()

    def init_simulation(self):
        for i in range(self.nb_villagers):
            self.add_villager()
        for i in range(int(self.nb_villagers / 100)):
            self.add_business()
        self.add_panel()
        self.add_storage()

    def step(self):
        self.step_production = 0
        self.m_step_production = 0
        self.produce()
        self.hospital_consumption()
        self.distribute_tokens()
        self.compute_needed_consumption()
        self.business_activities()
        if self.time % 24*30 == 0:
            self.pay_wages()
        self.trade()
        self.consume()
        self.store()
        self.time += 1
        print(len(Villager.market._ask), len(Villager.market._bid))

    def distribute_tokens(self):
        quantity = int(self.step_production / Token.KWH_PER_TOKEN)
        for _ in range(quantity):
            villager = self.villagers[self.current_token_id]
            villager.add_token(Token())
            if self.current_token_id == self.nb_villagers - 1:
                self.current_token_id = 0
            else:
                self.current_token_id += 1

    def business_activities(self):
        for b in self.businesses:
            b.generate_profit()

    def pay_wages(self):
        for b in self.businesses:
            b.pay_employees()

    def add_panel(self):
        self.panels.append(Panel())

    def add_storage(self):
        self.storages.append(Storage())

    def add_villager(self):
        villager = Villager(triangular(0, 1), triangular(0, 1))
        self.villagers.append(villager)

    def add_business(self):
        business = Business(triangular(0, 0.5), triangular(1, 2))
        self.businesses.append(business)
        unemployed = list(filter(lambda v: not v.employed, self.villagers))
        shuffle(unemployed)
        for _ in range(randint(1, len(unemployed) // 10)):
            business.add_employee(unemployed.pop())

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
        all_agents = self.villagers + self.businesses
        shuffle(all_agents)
        for agent in all_agents:
            agent.trade()

    def consume(self):
        for agent in self.villagers + self.businesses:
            agent.consume()

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
        hospital_consumption = offset + scale * scaled_gaussian(mu, var, t)
        delta = self.step_production - hospital_consumption
        if delta > 0:
            self.step_production -= hospital_consumption
        else:
            self.step_production = 0
            if self.take_from_storage(-delta) > 0:
                print("WE DONT HAVE ENOUGH ELECTRICITY FOR THE HOSPITAL!")
