# the rental class
from customer import Customer
from vehicle import EconomyCar, LuxuryCar, SUV, Vehicle

# a rental connects one customer to one vehicle
# customer + vehicle = Rental
# rental id can be auto generated
# customer = Customer():
# vehicle = [EconomyCar, LuxuryCar, SUV]
# rental_days = days
# actual_days are the days the car was actually kept
# status = [ACTIVE, COMPLETED, CANCELLED]
# base_cost -> obtains the value from one of the vehicle classes and 
# we get the rental_cost calculated based on the rental_days
class Rental(Customer, Vehicle):
    def __init__(self, rental_id, rental_days, actual_days, Customer, Vehicle):
        
        self.rental_id = rental_id
        self.customer = Customer
        self.vehicle = Vehicle
        self.rental_days = rental_days
        self.actual_days = actual_days
        self.status = "ACTIVE" 
        self.base_cost = Vehicle.calculate_rental_cost(rental_days)
        self.late_fee = 0.0
        self.damage_charge = 0.0
        self.__paid = False # private
        
        
        
    def calculate_late_fee(self):
        # works out the penalty for extra days
        late_days = self.actual_days - self.rental_days
        daily_late_penalty = self.vehicle.daily_rate * 0.2
        self.late_fee = late_days * daily_late_penalty
        return self.late_fee 
    
    def calculate_total(self):
        # returns the total cost of the renting, damages and days extended
        return self.base_cost + self.calculate_late_fee() + self.damage_charge
    
    def complete_rental(self, actual_days, damage_charge=0):
        # records the return and sets status to completed
        if actual_days == self.rental_days and damage_charge:
            self.status = 'COMPLETED'
        elif actual_days > self.rental_days:
            self.calculate_late_fee
        elif actual_days > self.rental_days and damage_charge > 0:
            self.calculate_total
         
    
    def mark_as_paid(self):
        return self.__paid == True
    
    def calculate_rental_cost(self, days):
        return super().calculate_rental_cost(days)
         
    
    def display_rental_details(self):
        print("=" * 40)
        print("          SAFARIDRIVE RENTALS          ")
        print("=" * 40)
        print(f"Rental ID: {self.rental_id:>12}")
        print(f"Customer: {self.customer.name:>15}")
        print(f"Vehicle: {self.vehicle.make:>23} {self.vehicle.model}")
        print(f"Registration: {self.vehicle.registration_number:>13}")
        print(f"Rental Period: {self.rental_days:>5} days")
        print(f"Daily Rate:        KSh {self.vehicle.daily_rate}")
        print()
        print()
        print(f"Rental Charge:     KSh {self.base_cost}")
        print(f"Service Charge:    KSh {self.vehicle.service_charge}")
        print("-" * 40)
        print(f"TOTAL:             KSh {self.calculate_total()}")
        print(f"Status: {self.status:>17}")
        print("=" * 40)
        


# customer1 = Customer("0101", "Leslie", "0712345678", "7575", "12345678")
# subaru = EconomyCar("KDA 9907", "Subaru", "Forester", "2015", 4000)
# mercedes = LuxuryCar("KDS 1111", "Mercedes Benz", "Sclass", "2020", 15000)

# safaridrive = Rental("R001", 3, 5, customer1, mercedes)
# # safaridrive.display_rental_details()
    