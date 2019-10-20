from random import triangular, shuffle, randint
from .Constants import KWH_PER_TOKEN, CONSUMPTIONS
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
        self.bank = randint(100, 10000)
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
        in_storage = self.total_stored()
        initial_tokens = in_storage / KWH_PER_TOKEN
        initial_tokens_per_habitant = int(initial_tokens / self.nb_villagers)
        for villager in self.villagers:
            for _ in range(initial_tokens_per_habitant):
                villager.add_token(Token())

    def step(self):
        print(self.time)
        print("Bank : ", self.bank)
        self.step_production = 0
        self.m_step_production = 0
        if self.time % 24 == 6:
            Villager.market.clean()
        self.produce()
        self.hospital_consumption()
        self.distribute_tokens()
        self.compute_needed_consumption()
        self.business_activities()
        if self.time % (24 * 30) == 0:
            self.pay_wages()
            self.hiring_process()
            self.bank += randint(10, 10000)
            repair_cost = 1000
            add_panel_cost = 30000
            for p in self.panels:
                if p.erosion > .1 and self.bank > repair_cost:
                    p.repare()
                    self.bank -= repair_cost

            if self.bank > add_panel_cost:
                self.add_panel()
                self.add_storage()
                self.bank -= add_panel_cost

        print("Grid numbers : ", len(self.panels))

        self.trade()
        self.consume()
        self.store()
        self.time += 1
        #print("ask:", len(Villager.market._ask), "bid:", len(Villager.market._bid))

    def distribute_tokens(self):
        quantity = int(self.step_production / KWH_PER_TOKEN)
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

    def hiring_process(self):
        unemployed = list(filter(lambda v: not v.employed, self.villagers))
        shuffle(unemployed)
        for b in self.businesses:
            b.hire_employees(unemployed)

    def add_panel(self):
        self.panels.append(Panel())

    def add_storage(self):
        self.storages.append(Storage())

    def total_stored(self):
        total = 0
        for storage in self.storages:
            total += storage.stock
        return total

    def add_villager(self):
        morning = triangular(0, .8)
        night = triangular(morning, 1 - morning)
        villager = Villager(morning, night)
        self.villagers.append(villager)

    def add_business(self):
        business = Business(triangular(0, 0.5), triangular(0, .5))
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
        offset = .4
        scale = .6
        mu = 13
        var = 4 ** 2
        hospital_consumption = (offset + scale * scaled_gaussian(mu, var, t)) * CONSUMPTIONS.HOSPITALS
        delta = self.step_production - hospital_consumption
        if delta > 0:
            self.step_production -= hospital_consumption
        else:
            self.step_production = 0
            if self.take_from_storage(-delta) > 0:
                print("WE DONT HAVE ENOUGH ELECTRICITY FOR THE HOSPITAL!")
