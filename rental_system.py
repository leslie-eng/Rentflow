from vehicle import Vehicle, EconomyCar, LuxuryCar, SUV
from customer import Customer
from rental import Rental
from payment import Payment, CardPayment, MpesaPayment


class CarRentalSystem:
    VEHICLE_TYPES = {
        "economy" : EconomyCar,
        "suv": SUV,
        "luxury":LuxuryCar
    }
    
    
    def __init__(self, name) -> None:
        self.name = name
        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []
        self.__revenue = 0 # private
    
    def __str__(self):
        return f"{self.name}: {len(self.vehicles)} vehicles, {len(self.customers)} customers"
    
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        
    def register_customer(self, customer):
        self.customers.append(customer)
    
    def find_vehicle(self, registration_number) -> None:
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None
    
    def find_customer(self, customer_id) -> None:
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
    
    def show_available_vehicles(self) -> None:
        for vehicle in self.vehicles:
            if vehicle.is_available():
               print(vehicle)
    
    def get_available_vehicles(self, vehicle_type, max_daily_rate=None):
        vehicle_class = self.VEHICLE_TYPES.get(vehicle_type.strip().lower())
        if vehicle_class is None:
           raise ValueError(f"Unknown vehicle type: {vehicle_type}")
        
        results = [
                      v for v in self.vehicles
                     if isinstance(v, vehicle_class)
                     and (max_daily_rate is None or v.daily_rate <= max_daily_rate)
                     ]
        return results
    
    def search_vehicles(self, vehicle_type, max_daily_rate=None):
        results = self.get_available_vehicles(vehicle_type=vehicle_type, max_daily_rate=max_daily_rate)

        print(f"AVAILABLE {vehicle_type.upper()}S")
        if not results:
               print("   No matching vehicles found.")
               return results

        for num, vehicle in enumerate(results, start=1):
            print()
            print(f"{num}. {vehicle.make} {vehicle.model}")
            print(f"   Registration: {vehicle.registration_number}")
            print(f"   Rate: Ksh {vehicle.daily_rate}/day")

        return results
    
    def rent_vehicle(self, customer, vehicle, days):
       # check if the customer is registered
       cus_id = customer.customer_id
       if self.find_customer(customer_id=cus_id) is None:
           raise ValueError("Customer has to be registered to rent a car !")
       
       # check is the car is available
       if not vehicle.is_available():
           raise ValueError("Vehicle is not available please try another one")
       
       rental = Rental(
                  rental_id=f"R{len(self.rentals) + 1:03d}",
                  rental_days=days,
                  actual_days=days,
                  Customer=customer,
                  Vehicle=vehicle
              )
       rental.mark_as_rented()
       self.rentals.append(rental)
       customer.add_rental(rental)
       return rental
    
    def return_vehicle(self, rental, actual_days, damage_charge=0):
        rental.complete_rental(actual_days=actual_days, damage_charge=damage_charge)
        rental.status = 'COMPLETED'
        rental.mark_as_available()
        return self.show_available_vehicles()
    
    def process_payment(self, payment):
        # we have 3 types of payment and we only need to show it being processed
        self.payments.append(payment.amount)
        paid = payment.process_payment()
        self.__revenue += payment.amount
        return paid
    
    def show_active_rentals(self):
        for rental in self.rentals:
            if rental.status == "ACTIVE":
                return rental
                
    
    def show_completed_rentals(self):
        for rental in self.rentals:
            if rental == "COMPLETED":
                return rental
            
    
    @property
    def revenue(self):
        return self.__revenue
        
    
    def generate_report(self):
        print("=" * 40)
        print("     SAFARIDRIVE MANAGEMENT REPORT   ")
        print("=" * 40)
        print(f"Total Vehicles: {len(self.vehicles):>15}")
        print(f"Available Vehicles: {len([v for v in self.vehicles if v.is_available()]):>11}")
        print(f"Rented Vehicles: {len(self.rentals):>14}")
        print()
        print()
        print(f"Registered Customers: {len(self.customers):>9}")
        print()
        print()
        print(f"Total Rentals: {len(self.rentals):>16}")
        print(f"Active Rentals: {len([self.show_active_rentals()]):>15}")
        print(f"Completed Rentals: {len([self.show_available_vehicles()]):>12}")
        print()
        print()
        print(f"Total Revenue:      Ksh {self.revenue}")
        print("-" * 40)
        print("VEHICLES BY CATEGORY")
        print(f"Economy Cars: {len(self.get_available_vehicles(vehicle_type="economy")):>16}")
        print(f"SUVs: {len(self.get_available_vehicles(vehicle_type="SUV")):>24}")
        print(f"Luxury Cars: {len(self.get_available_vehicles(vehicle_type="luxury")):>17}")
        print("=" * 40)
        
        
# rent = CarRentalSystem(name="Safari Drive Rentals")

# # testing the economy car
# subaru = EconomyCar("KDA 9907", "Subaru", "Forester", "2015", 4000)
# LandCruizer = SUV("KDZ 9988", "Land Cruzier", "Prado", "2020", 15000)
# customer1 = Customer("0101", "Leslie", "0712345678", "7575", "12345678")
# rent.add_vehicle(vehicle=subaru)
# rent.add_vehicle(vehicle=LandCruizer)
# rent.register_customer(customer=customer1)
# # rental = rent.rent_vehicle(customer=customer1, vehicle="economy", days=5)
# # rent.search_vehicles("economy")
# # print(rent.rent_vehicle(customer=customer1, vehicle=LandCruizer, days=5))
# # print(rent.find_vehicle(registration_number="KDZ 9988"))
# # rent.find_customer(customer_id="0101")
# # rent.show_available_vehicles()
# # rent.search_vehicles(vehicle_type="SUV")
# rental1 = rent.rent_vehicle(customer=customer1, vehicle=LandCruizer, days=5)
# payment1 = CardPayment(card="126543768", rental=rental1)
# # rent.return_vehicle(rental=rental1, actual_days=4)
# # rent.show_completed_rentals()
# # print(rent.revenue)

# rent.process_payment(payment=payment1)


# rent.generate_report()