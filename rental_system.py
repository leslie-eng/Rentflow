

class CarRentalSystem:
    def __init__(self) -> None:
        self.name = "SafariDrive Rentals"
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []
        self.__revenue = 0
        
    def add_vehicles(self, vehicle):
        pass
    
    def register_customer(self, customer):
        pass
    
    def find_vehicle(self, registration_number):
        pass
    
    def find_customer(self, customer_id):
        pass
    
    def show_available_vehicles(self):
        pass
    
    def search_vehicles(self, vehicle_type=None, max_daily_rate=None):
        pass
    
    def rent_vehicles(self, customer, vehicle, days):
        pass
    
    def return_vehicle(self, rental, actual_days, damage_charge=0):
        pass
    
    def process_payment(self, payment):
        pass
    
    def show_active_rentals(self):
        pass
    
    def show_completed_rentals(self):
        pass
    
    @property
    def revenue(self):
        pass 
    
    def generate_report(self):
        print("=" * 50)
        print("   SAFARIDRIVE MANAGEMENT REPORT   ")
        print("=" * 50)
        print(f"Total Vehicles: {len(self.vehicles):>15}")
        print(f"Available Vehicles: {self.rentals}")
        print(f"Rented Vehicles: {self.rentals}")
        print()
        print()
        print(f"Registered Customers: {len(self.customers):>15}")
        print()
        print()
        print(f"Total Rentals: {self.rentals:>15}")
        print(f"Active Rentals: {len(self.rentals):>15}")
        print(f"Completed Rentals: {self.rentals:>15}")
        print()
        print()
        print(f"Total Revenue: Ksh {self.revenue}")
        print("-" * 50)
        print("VEHICLES BY CATEGORY")
        print(f"Economy Cars: {len(self.rentals):>15}")
        print(f"SUVs: {self.rentals:>15}")
        print(f"Luxury Cars: {self.rentals:>15}")
        print("=" * 50)
        
        
rent = CarRentalSystem().generate_report()
print(rent)