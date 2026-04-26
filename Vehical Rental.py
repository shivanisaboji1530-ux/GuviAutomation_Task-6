class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days


# Car class
class Car(Vehicle):
    def __init__(self, model, rental_rate, fuel_type):
        super().__init__(model, rental_rate)
        self.fuel_type = fuel_type

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        insurance_fee = 300  # fixed charge
        return base_cost + insurance_fee


# Bike class
class Bike(Vehicle):
    def __init__(self, model, rental_rate, cc):
        super().__init__(model, rental_rate)
        self.cc = cc

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        if days > 5:
            discount = 0.15 * base_cost
            return base_cost - discount
        return base_cost


# Truck class
class Truck(Vehicle):
    def __init__(self, model, rental_rate, capacity):
        super().__init__(model, rental_rate)
        self.capacity = capacity

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        load_charge = 800  # extra for heavy vehicles
        return base_cost + load_charge


# ------------------ Usage ------------------

vehicles = [
    Car("Kia Syros", 2500, "Petrol"),
    Bike("Mahindra", 700, 170),
    Truck("Tata Sierra", 6500, "10 Tons")
]

days = 4

for v in vehicles:
    cost = v.calculate_rental(days)
    print(f"{v.model} rental for {days} days: {cost}")