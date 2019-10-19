from .Villager import Villager

CONS_OFFSET = 0.1
MAX_CONS = 2


class Business(Villager):
    def __init__(self, fixed_consumption, variable_consumption):
        super().__init__(0, 0)
        self.fixed_consumption = fixed_consumption
        self.variable_consumption = variable_consumption

    def needed_consumption_update(self, time):
        t = time % 24

        if t < 7 or t > 19:
            self.needed_consumption = self.fixed_consumption

        elif t == 8 or t == 18:
            self.needed_consumption = (self.fixed_consumption+self.variable_consumption)/2

        else:
            self.needed_consumption = self.variable_consumption
