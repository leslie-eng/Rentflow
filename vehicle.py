from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, registration_number, make, model, year, daily_rate):
        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative")
        
        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year 
        self.daily_rate = daily_rate
        self.__available = True
        self.service_charge = 0.0
    
        
    def display_details(self):
        print(f"car make: {self.make}, model: {self.model}, year: {self.year}, reg number: {self.registration_number}, daily rate: {self.daily_rate}")
        
    def is_available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False
    
    def mark_as_available(self):
        self.__available = True 
    
    @abstractmethod
    def calculate_rental_cost(self, days):
        pass
        
   
   
# EconomyCar class
class EconomyCar(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate)
        
    def calculate_rental_cost(self, days):
        return self.daily_rate * days
    

# SUV class
class SUV(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate)
        self.service_charge = 2000
        
    def calculate_rental_cost(self, days):
        return self.daily_rate * days + self.service_charge
    
# LuxuryCar class
class LuxuryCar(Vehicle):
    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(registration_number, make, model, year, daily_rate) 
        
    def calculate_rental_cost(self, days):
        # 10% insurance on that amount
        flat_rate = self.daily_rate * days 
        return flat_rate + (0.1 * flat_rate)
       
        
#testing the vehicle class and expected output
# you can't use an abstract class because it is meant to be subclassed
# subaru = Vehicle("KDA 9907", "Subaru", "Forester", "2015", 20)
# print(subaru.display_details())
# print(subaru.is_available())
# print(subaru.mark_as_rented())
# print(subaru.mark_as_available())

# # testing the economy car
# subaru = EconomyCar("KDA 9907", "Subaru", "Forester", "2015", 4000)
# print(subaru.display_details())
# print(subaru.calculate_rental_cost(10))
# print("#" * 20)

# # testing the suv car
# LandCruizer = SUV("KDZ 9988", "Land Cruzier", "Prado", "2020", 15000)
# print(LandCruizer.display_details())
# print(LandCruizer.calculate_rental_cost(5))
# print(LandCruizer.service_charge)

# # testing the luxury car
# sclass = LuxuryCar("KDG 0998", "Benz", "Sclass", "2015", 20000)
# print(sclass.display_details())
# print(sclass.calculate_rental_cost(20))

