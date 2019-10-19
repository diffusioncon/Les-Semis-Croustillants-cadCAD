from .Panel import Panel
from .Storage import Storage

TOKEN_PER_KILLOWAT = 0


class Central:
    def __init__(self):
        self.panels = []
        self.storages = []
        self.cash = []

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
                quantity = storage.fill(quantity)
            else:
                break
        self.distribute_tokens((total_produced - quantity) / 100)

    def distribute_tokens(self, quantity):
        # Give N tokens to each villager
        pass
