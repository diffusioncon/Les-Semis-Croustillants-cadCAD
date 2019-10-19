from .Villager import Villager

CONS_OFFSET = 0.1
MAX_CONS = 2

class Business(Villager):
    def __init__(self):
        super().__init__()
        self.needed_consumption = 0
        pass

    def consumption(self):
        pass

    def needed_consumption_update(self, time, offset=CONS_OFFSET, max_cons=MAX_CONS):
        t = time % 24

        if t < 7 or t > 19:
            self.needed_consumption = offset

        elif t == 8 or t == 18:
            self.needed_consumption = (offset+max_cons)/2

        else:
            self.needed_consumption = max_cons
