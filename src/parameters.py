from agents import Villager


class Parameters:
    def __init__(self, central):
        self.central = central
        self.partial_state_update_blocks = {}
        self.set_partial_state_update_blocks()

    def initial_state(self):
        return {
            "step": 0,
            "time": 7,
            "production": 0,
            "villagers_consumption": 0,
            "businesses_consumption": 0,
            "hospital_consumption": 0,
            "grids": 0,
            "bank": 0,
            "bid": 0,
            "ask": 0,
            "price": 0
        }

    @staticmethod
    def step(central):
        def closure(*_):
            central.step()
            return "step", 0

        return closure

    def get_time(self):
        def closure(*_):
            return "time", self.central.time

        return closure

    def get_production(self):
        def closure(*_):
            return "production", self.central.m_step_production

        return closure

    def get_villagers_consumption(self):
        def closure(*_):
            return "villagers_consumption", self.central.m_villagers_consumption

        return closure

    def get_businesses_consumption(self):
        def closure(*_):
            return "businesses_consumption", self.central.m_businesses_consumption

        return closure

    def get_hospital_consumption(self):
        def closure(*_):
            return "hospital_consumption", self.central.m_hospital_consumption

        return closure

    def get_grids(self):
        def closure(*_):
            return "grids", len(self.central.panels)

        return closure

    def get_bank(self):
        def closure(*_):
            return "bank", self.central.bank

        return closure

    @staticmethod
    def get_bid():
        def closure(*_):
            return "bid", len(Villager.market._bid)
        return closure

    @staticmethod
    def get_ask():
        def closure(*_):
            return "ask", len(Villager.market._ask)
        return closure

    @staticmethod
    def get_price():
        def closure(*_):
            return "price", Villager.market.last_price
        return closure

    def set_partial_state_update_blocks(self):
        step = self.step(self.central)
        get_time = self.get_time()
        get_production = self.get_production()
        get_villagers_consumption = self.get_villagers_consumption()
        get_businesses_consumption = self.get_businesses_consumption()
        get_hospital_consumption = self.get_hospital_consumption()
        get_grids = self.get_grids()
        get_bank = self.get_bank()
        get_bid = self.get_bid()
        get_ask = self.get_ask()
        get_price = self.get_price()
        self.partial_state_update_blocks = [
            {
                "policies": {},
                'variables': {  # The following state variables will be updated simultaneously
                    "step": step
                }
            },
            {
                "policies": {},
                "variables": {
                    "time": get_time,
                    "production": get_production,
                    "villagers_consumption": get_villagers_consumption,
                    "businesses_consumption": get_businesses_consumption,
                    "hospital_consumption": get_hospital_consumption,
                    "grids": get_grids,
                    "bank": get_bank,
                    "bid": get_bid,
                    "ask": get_ask,
                    "price": get_price
                }
            }
        ]
