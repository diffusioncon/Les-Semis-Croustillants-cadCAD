class Token:
    def __init__(self):
        self.owner = None
        self.on_market = False

    def put_on_market(self):
        self.on_market = True

    def remove_from_market(self):
        self.on_market = False

    def __lt__(self, other):
        return True
