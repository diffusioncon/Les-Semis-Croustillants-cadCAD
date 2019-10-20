from random import randint
import math
from .Villager import Villager
from .Constants import CONSUMPTIONS

MINIMUM_WAGE = 70


class Business(Villager):
    real_consumption = CONSUMPTIONS.BUSINESSES

    def __init__(self, fixed_consumption, variable_consumption):
        super().__init__(0, 0)
        self.fixed_consumption = fixed_consumption
        self.variable_consumption = variable_consumption
        self.bank = 100000
        self.can_hire = 0
        self.employees = set()

    def needed_consumption_update(self, time):
        t = time % 24
        if t < 7 or t > 19:
            self.needed_consumption = self.fixed_consumption
        elif t == 8 or t == 18:
            self.needed_consumption = (self.fixed_consumption + self.variable_consumption) / 2
        else:
            self.needed_consumption = self.variable_consumption

    def add_employee(self, employee):
        self.employees.add(employee)
        employee.employed = True

    def remove_employee(self, employee):
        self.employees.remove(employee)
        employee.employed = False

    def generate_profit(self):
        tokens_needed = self.tokens_needed()
        total_tokens = len(self.tokens)
        max_profit_electricity = 1000 + 100 * len(self.employees)
        max_profit = max_profit_electricity if total_tokens >= tokens_needed else int(
            (total_tokens / tokens_needed) * max_profit_electricity)
        self.bank += randint(0, 50 + max_profit)

    def fire_employees(self, count):
        if count >= len(self.employees):
            count = len(self.employees) - 2
        employees_tuple = tuple(self.employees)
        for i in range(count):
            self.remove_employee(employees_tuple[i])

    def hire_employees(self, unemployed):
        for employee in range(self.can_hire):
            if len(unemployed):
                self.add_employee(unemployed.pop())
            else:
                return

    def pay_employees(self):
        total_wages = len(self.employees) * MINIMUM_WAGE
        if self.bank >= total_wages:
            for employee in self.employees:
                employee.credit(MINIMUM_WAGE)
                self.bank -= MINIMUM_WAGE
            self.can_hire = int((self.bank / MINIMUM_WAGE) * .2)
        else:
            print(len(self.employees))
            self.fire_employees(abs(math.ceil((self.bank - total_wages) / MINIMUM_WAGE)))
            print(len(self.employees))
            self.can_hire = 0
            print("CAN'T PAY EMPLOYEES", self.bank)
