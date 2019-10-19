from .functions import scaled_gaussian

EROSION_RATE = .005/24


class Panel:
    def __init__(self, hourly_erosion_rate=EROSION_RATE):
        self.production_per_period = 1
        self.erosion = 0
        self.hourly_erosion_rate = hourly_erosion_rate

    def produce(self, time):
        self.erosion += self.hourly_erosion_rate
        return self.production_per_period*(1-self.erosion)*self.hour_prod(time)

    def repare(self):
        self.erosion = 0

    @staticmethod
    def hour_prod(time):
        # return a value between 0 and 1 corresponding to the solar pannel
        # percentage production comparing to the max production,
        # depending of the day hour'''
        t = time % 24
        if t < 7 or t > 19:
            return 0

        else:
            mu = 13
            var = 9
            return scaled_gaussian(mu, var, t)
