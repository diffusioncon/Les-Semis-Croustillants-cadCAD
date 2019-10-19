class Storage:
    def __init__(self, max_stock):
        self.stock = max_stock
        self.max_stock = max_stock

    def fill(self, quantity):
        free = self.max_stock - self.stock
        if quantity >= free:
            self.stock += quantity
            return 0
        quantity -= free
        self.stock += quantity
        return quantity
