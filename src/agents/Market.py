from heapq import heappush, heappop


class Market:
    _bid = []
    _ask = []
    last_price = 0

    def ask(self, token, price):
        heappush(self._ask, (price, token))

    def bid(self, villager, price, quantity):
        while len(self._ask) and self._ask[0][0] <= price:
            price, token = heappop(self._ask)
            villager.add_token(token)
            villager.debit(price)
            owner = token.owner
            owner.credit(price)
            owner.remove_token(token)
        heappush(self._bid, (price, quantity))
