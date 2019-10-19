MAX_PER_STORAGE = 10000


class Storage:
    def __init__(self, max_stock=MAX_PER_STORAGE):
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

    def take(self, quantity):
        if quantity > self.stock:
            quantity -= self.stock
            self.stock = 0
            return quantity
        self.stock -= quantity
        return 0
