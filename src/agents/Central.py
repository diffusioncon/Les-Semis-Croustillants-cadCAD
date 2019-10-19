from .Panel import Panel
from .Storage import Storage


class Central:
    def __init__(self, token_per_kW, nb_villagers):
        self.panels = []
        self.storages = []
        self.cash = []
        self.token_per_kW = token_per_kW
        self.nb_villagers = nb_villagers

    def add_panel(self):
        self.panels.append(Panel())

    def add_storage(self):
        self.storages.append(Storage())

    def produce(self):
        total_produced = 0
        for panel in self.panels:
            total_produced += panel.produce()
        quantity = total_produced
        for storage in self.storages:
            if quantity:
                quantity = storage.fill()
        self.distribute_tokens((total_produced - quantity) / self.nb_villagers)

    def distribute_tokens(self, quantity):
        # Give N tokens to each villager
        pass
