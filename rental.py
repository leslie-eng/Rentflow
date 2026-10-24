# the rental class
from customer import Customer
from vehicle import Vehicle, EconomyCar, LuxuryCar, SUV

customer1 = Customer("0101", "Leslie", "0712345678", "7575", "12345678")
subaru = EconomyCar("KDA 9907", "Subaru", "Forester", "2015", 4000)
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
class Rental(Customer, EconomyCar):
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
        self.service_charge = 0.0
        
        
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
            return self.status == 'COMPLETED'
        elif actual_days > self.rental_days:
            self.calculate_late_fee
        elif actual_days > self.rental_days and damage_charge > 0:
            self.calculate_total
         
    
    def is_paid(self):
        pass
         
    
    def display_rental_details(self):
        print("=" * 50)
        print("          SAFARIDRIVE RENTALS          ")
        print("=" * 50)
        print(f"Rental ID: {self.rental_id:>16}")
        print(f"Customer: {self.name}")
        print(f"Vehicle: {self.make} {self.model}")
        print(f"Registration: {self.registration_number}")
        print(f"Rental Period: {self.rental_days} days")
        print(f"Daily Rate: KSh {self.daily_rate}")
        print()
        print()
        print(f"Rental Charge: KSh {self.base_cost}")
        print(f"Service Charge: KSh {self.service_charge}")
        print("-" * 50)
        print(f"TOTAL: KSh {self.calculate_total()}")
        print(f"Status: {self.status}")
        print("=" * 50)
        

safaridrive = Rental("R001", 5, 5, customer1, subaru)
safaridrive.display_rental_details()
    