

class Customer:
    def __init__(self, customer_id, name, phone_number, national_id, driving_licence):
        self.customer_id = customer_id
        self.name = name
        self.phone_nummber = phone_number
        self.national_id = national_id
        self.driving_licence = driving_licence
        self.rentals = []
        
    def display_details(self):
        print(f"Customer name {self.name} with customer id {self.customer_id}, phone number {self.phone_nummber}, national id {self.national_id} and driving licence {self.driving_licence}") 
        
        
    def add_rental(self, rental):
        return self.rentals.append(rental)
    
    def view_rental_history(self):
        return [f"{rental}" for rental in self.rentals] 
    
    

## test script to check if it works
customer1 = Customer("0101", "Leslie", "0712345678", "7575", "DL7865")
print(customer1.display_details())
           

