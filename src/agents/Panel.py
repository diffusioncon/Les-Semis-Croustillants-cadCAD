class Panel:
    def __init__(self):
        self.production_per_period = 1
        self.erosion = 0

    def produce(self):
        self.erosion += .01
        return self.production_per_period

    def repare(self):
        self.erosion = 0
