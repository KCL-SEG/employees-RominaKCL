"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:

    def __init__(self, name, salary_contract, commission, fixed_commision, monthly_salary, work_hours, hourly_wage, fixed_bonus, contract_numbers, contract_commission):
        self.name = name+" works on a "
        self.salary_Contract = salary_contract
        self.commission = commission
        self.fixed_comssion = fixed_commision
        self.monthly_salary = monthly_salary
        self.work_hours = work_hours
        self.hourly_wage = hourly_wage
        self.fixed_bonus = fixed_bonus
        self.contract_numbers = contract_numbers
        self.contract_commission = contract_commission

    def calculate_bonus(self):
        if self.commission:
            self.name += " and receives a "
            if self.fixed_comssion:
                self.name += "bonus commission of "+str(self.fixed_bonus)
                return self.fixed_bonus
            else:
                self.name += "commission for " + \
                    str(self.contract_numbers)+" contract(s) at " + str(self.contract_commission)+"/contract"
                return self.contract_numbers*self.contract_commission
        else:
            return 0

    def get_pay(self):
        total = 0
        if self.salary_Contract:
            self.name += "monthly salary of "+str(self.monthly_salary)
            total += self.monthly_salary + self.calculate_bonus()
        else:
            self.name += "contract of " + \
                str(self.work_hours)+" hours at "+str(self.hourly_wage)+"/hour"
            total += self.work_hours*self.hourly_wage+self.calculate_bonus()
        return total

    def __str__(self):
        self.name += ". Their total pay is "+str(self.get_pay())+"."
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, False, False, 4000, 0, 0, 0, 0, 0)
print(str(billie))
# print(billie.get_pay())

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, False, False, 0, 100, 25, 0, 0, 0)
print(str(charlie))
# print(charlie.get_pay())

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, True, False, 3000, 0, 0, 0, 4, 200)
print(str(renee))
# print(renee.get_pay())

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, True, False, 0, 150, 25, 0, 3, 220)
print(str(jan))
# print(jan.get_pay())

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, True, True, 2000, 0, 0, 1500, 0, 0)
print(str(robbie))
# print(robbie.get_pay())

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, True, True, 0, 120, 30, 600, 0, 0)
print(str(ariel))
# print(ariel.get_pay())
