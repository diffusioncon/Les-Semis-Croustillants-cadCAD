class Storage:
    def __init__(self):
        self.stock = 0
        self.max_stock = 0

    def fill(self, quantity):
        free = self.max_stock - self.stock
        if quantity >= free:
            self.stock += quantity
            return 0
        quantity -= free
        self.stock += quantity
        return quantity
