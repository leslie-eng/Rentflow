# payment class

from abc import ABC, abstractmethod
import random
from rental import Rental
import string
import time
import random

class Payment(ABC):
    rental = Rental()
    amount = rental.calculate_total()
    
    @abstractmethod
    def process_payment(self):
        pass
    
class MpesaPayment(Payment):
    
    def __init__(self) -> None:
        self.phone_number = rental.phone_number
    
    def process_payment(self):
        # genereates a transaction code and prints a confirmation
        capital_letters = list(string.ascii_uppercase)
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        let_numbers = capital_letters + numbers
        transcode = [random.choice(let_numbers) for _ in range(10)]
        print("Processing M-Pesa payment...")
        time.sleep(3)
        print(f"Transaction: {"".join(transcode)}")
        print("Payment of Ksh {amount} successful.")
        

class CardPayment(Payment):

    def process_payment(self, card):
        if not card or not str(card).strip():
            raise ValueError("Card can't be empty")
        
        return f" Card ending {card[-4:]} charged Ksh {self.amount}"

class CashPayment(Payment):
    def process_payment(self, cash):
        change = 0.0
        change = cash - self.amount
        if change < 0:
           print(f"You are expected to clear a balance of Ksh {change}")
        elif change == 0.0:
           print(f"Cash received: Ksh {cash}")
           print(f"Change due: Ksh {change}")
        else:
           print(f"Cash received: Ksh {cash:>5}")
           print(f"Change due: Ksh {change:>10}")
           print(f"Cash payment of Ksh {self.amount} recorded")
         
   