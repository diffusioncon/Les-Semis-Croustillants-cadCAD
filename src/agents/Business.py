from random import randint
from .Villager import Villager

CONS_OFFSET = 0.1
MAX_CONS = 2
MINIMUM_WAGE = 70


class Business(Villager):
    def __init__(self, fixed_consumption, variable_consumption):
        super().__init__(0, 0)
        self.fixed_consumption = fixed_consumption
        self.variable_consumption = variable_consumption
        self.bank = 100000
        self.employees = set()

    def needed_consumption_update(self, time):
        t = time % 24
        if t < 7 or t > 19:
            self.needed_consumption = self.fixed_consumption
        elif t == 8 or t == 18:
            self.needed_consumption = (self.fixed_consumption+self.variable_consumption)/2
        else:
            self.needed_consumption = self.variable_consumption

    def add_employee(self, employee):
        self.employees.add(employee)
        employee.employed = True

    def generate_profit(self):
        self.bank += randint(0, 50)

    def pay_employees(self):
        for employee in self.employees:
            employee.add_cash(MINIMUM_WAGE)
            self.bank -= MINIMUM_WAGE
