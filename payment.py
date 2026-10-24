# payment class
from abc import ABC, abstractmethod
import random
from rental import Rental
from vehicle import EconomyCar, LuxuryCar
from customer import Customer
import string
import time
import random

class Payment(ABC):
    def __init__(self, rental) -> None:
        self.rental = rental
        self.amount = rental.calculate_total()
        
        
    @abstractmethod
    def process_payment(self) -> bool:
        pass
    
class MpesaPayment(Payment):
    
    def __init__(self, phone_number, rental) -> None:
        super().__init__(rental)
        self.phone_number = phone_number
        self.amount = rental.calculate_total()
    
    def process_payment(self):
        # genereates a transaction code and prints a confirmation
        capital_letters = list(string.ascii_uppercase)
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        let_numbers = capital_letters + numbers
        transcode = [random.choice(let_numbers) for _ in range(10)]
        print("Processing M-Pesa payment...")
        time.sleep(3)
        print(f"Transaction: {"".join(transcode)}")
        print(f"Payment of Ksh {self.amount} successful.")
        return True
        

class CardPayment(Payment):
    def __init__(self, card, rental) -> None:
        super().__init__(rental)
        if not card or not str(card).strip():
                    raise ValueError("Card can't be empty")
        self.card = card

    def process_payment(self):
        print(f" Card ending {self.card[-4:]} charged Ksh {self.amount}")
        return True

class CashPayment(Payment):
    def __init__(self, cash, rental) -> None:
        super().__init__(rental)
        self.cash = cash
        self.change = 0.0
        
    def process_payment(self):
        self.change = self.cash - self.amount
        if self.change < 0:
           print(f"You are expected to clear a balance of Ksh {self.change}")
           return False
        elif self.change == 0.0:
           print(f"Cash received: Ksh {self.cash}")
           print(f"Change due: Ksh {self.change}")
           return True
        else:
           print(f"Cash received:   Ksh {self.cash}")
           print(f"Change due:      Ksh {self.change}")
           print(f"Cash payment of  Ksh {self.amount} recorded")
           return True
         

customer1 = Customer("0101", "Leslie", "0712345678", "7575", "12345678")
subaru = EconomyCar("KDA 9907", "Subaru", "Forester", "2015", 4000)
mercedes = LuxuryCar("KDS 1111", "Mercedes Benz", "Sclass", "2020", 15000)

safaridrive = Rental("R001", 3, 5, customer1, mercedes)

# Mpesa = MpesaPayment("0707700995", safaridrive)
# Mpesa.process_payment()

# card = CardPayment("41236789", safaridrive)
# card.process_payment()

cash = CashPayment(cash=100000, rental=safaridrive)
cash.process_payment()