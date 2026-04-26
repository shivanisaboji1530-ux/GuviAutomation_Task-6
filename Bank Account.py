class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance   # encapsulated (private)

    # getter method
    def get_balance(self):
        return self.__balance

    # deposit method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # withdraw method (basic check)
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")


# Savings Account (inherits BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Interest: {interest}")
        return interest


# Current Account (inherits BankAccount)
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    # override withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.get_balance() - amount < self.min_balance:
            print("Cannot withdraw: Minimum balance requirement not maintained")
        else:
            # accessing parent private balance via deposit logic
            remaining = self.get_balance() - amount
            self._BankAccount__balance = remaining
            print(f"Withdrawn: {amount}")


# ------------------ Usage ------------------

# Savings Account
savings = SavingsAccount("SA123", 1000, 5)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()
print("Final Balance:", savings.get_balance())

print("------")

# Current Account
current = CurrentAccount("CA456", 2000, 500)
current.deposit(300)
current.withdraw(1800) # should fail due to min balance
current.withdraw(1000) # valid
print("Final Balance:", current.get_balance)
