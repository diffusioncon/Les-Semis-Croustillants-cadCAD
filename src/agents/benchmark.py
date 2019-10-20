"""
class BenchMark:
    def __init__(self, name):
        self.name = name
        self.start_time = time.time()

    def end(self):
        print("%s took %s seconds" % (self.name, time.time() - self.start_time))

    def step(self):
        self.step_production = 0
        self.m_step_production = 0
        benchmark = BenchMark("produce")
        self.produce()
        benchmark.end()
        benchmark = BenchMark("hospital")
        self.hospital_consumption()
        benchmark.end()
        benchmark = BenchMark("distribute")
        self.distribute_tokens()
        benchmark.end()
        benchmark = BenchMark("consumption needed")
        self.compute_needed_consumption()
        benchmark.end()
        benchmark = BenchMark("business")
        self.business_activities()
        if self.time % 24*30 == 0:
            self.pay_wages()
        benchmark.end()
        benchmark = BenchMark("trade")
        self.trade()
        benchmark.end()
        benchmark = BenchMark("consume")
        self.consume()
        benchmark.end()
        benchmark = BenchMark("store")
        self.store()
        benchmark.end()
        self.time += 1
        print(len(Villager.market._ask), len(Villager.market._bid))
"""