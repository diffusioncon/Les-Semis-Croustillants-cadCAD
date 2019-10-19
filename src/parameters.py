class Parameters:
    def __init__(self, central):
        self.central = central
        self.partial_state_update_blocks = {}
        self.set_partial_state_update_blocks()

    def initial_state(self):
        return {
            "central": self.central,
            "day": 0
        }

    @staticmethod
    def step(central):
        def closure(*_):
            central.step()
            return ("day", 0)

        return closure

    def set_partial_state_update_blocks(self):
        step = self.step(self.central)
        self.partial_state_update_blocks = [
            {
                "policies": {},
                'variables': {  # The following state variables will be updated simultaneously
                    "day": step
                }
            }
        ]
