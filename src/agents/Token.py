class Token:
    KWH_PER_TOKEN = 1

    def __init__(self):
        self.owner = None
        self.on_market = False

    def put_on_market(self):
        self.on_market = True

    def remove_from_market(self):
        self.on_market = False
