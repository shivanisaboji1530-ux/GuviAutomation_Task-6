class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# Regular Employee
class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        total = self.base_salary + self.bonus
        return total


# Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total = self.hourly_rate * self.hours_worked
        return total


# Manager
class Manager(Employee):
    def __init__(self, name, base_salary, allowance):
        super().__init__(name, base_salary)
        self.allowance = allowance

    def calculate_salary(self):
        total = self.base_salary + self.allowance
        return total


# ------------------ Usage ------------------

emp1 = RegularEmployee("Shivani", 40000, 6000)
emp2 = ContractEmployee("Rakesh", 800, 70)
emp3 = Manager("Kirthana", 40000, 20000)

employees = [emp1, emp2, emp3]

for emp in employees:
    print(f"Name: {emp.name}, Salary: {emp.calculate_salary()}")