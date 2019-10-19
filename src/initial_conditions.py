class initial_conditions:
    def __init__(self, central):
        self.central = central

    def get(self):
        return {
            "central": self.central
        }
