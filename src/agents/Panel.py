class Panel:
    def __init__(self, hourly_erosion_rate):
        self.production_per_period = 1
        self.erosion = 0
        self.hourly_erosion_rate = hourly_erosion_rate

    def produce(self):
        self.erosion += self.hourly_erosion_rate
        return self.production_per_period*(1-self.erosion)*f(t)

    def repare(self):
        self.erosion = 0
