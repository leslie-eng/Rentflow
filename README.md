# RentFlow / SafariDrive Rentals

RentFlow is a small Python object-oriented car-rental demonstration built around vehicles, customers, rentals, payments, and a central rental manager. It runs entirely in memory and includes Economy, SUV, and Luxury vehicle types.

## Features

- Add vehicles and register customers.
- Display available vehicles or filter by vehicle type and maximum daily rate.
- Create rentals for registered customers.
- Track vehicle availability and customer rental history.
- Calculate base rental charges with vehicle-specific pricing rules:
  - Economy: daily rate × rental days.
  - SUV: daily rate × rental days plus a KSh 2,000 service charge.
  - Luxury: daily rate × rental days plus 10% insurance.
- Return vehicles and record late and damage charges.
- Process M-Pesa, card, or cash payments.
- Print a management summary with vehicle counts and revenue.

## How It Works

`main.py` is a runnable example of the complete flow:

1. `CarRentalSystem` creates an in-memory rental system named “SafariDrive Rentals.”
2. Economy, SUV, and Luxury vehicles are added to the system.
3. A `Customer` is registered.
4. A vehicle is rented for a number of days by creating a `Rental`.
5. Renting marks the vehicle unavailable; returning it makes it available again.
6. `Rental` calculates the base cost, late fee, damage charge, and total.
7. A payment implementation processes the amount and updates the system revenue.

The diagram `rentflow.drawio` provides an additional visual representation of the model.

## Project Structure

```text
rentflow/
├── main.py             # Runnable demo
├── rental_system.py    # Central vehicle, customer, rental, and payment manager
├── vehicle.py          # Abstract Vehicle and economy, SUV, luxury subclasses
├── customer.py         # Customer details and rental history
├── rental.py           # Rental costs, status, and late/damage calculations
├── payment.py          # Payment base class and M-Pesa, card, and cash implementations
├── rentflow.drawio     # Project class/flow diagram
└── rentflow/
    └── test_code.py    # Additional rental example
```

## Prerequisites

- Python 3
- No third-party Python packages are required by the application.

## Run the Example

From the `rentflow` directory, run:

```bash
python main.py
```

The example adds four vehicles, registers John Kamau, rents a Toyota Prado, attempts to rent the Prado again while unavailable, and returns it for payment processing and reporting.

> [!WARNING]
> The current `main.py` demo does not complete successfully: `MpesaPayment` is defined with `(phone_number, rental)`, but the example calls it with `(rental1, "0712345678")`. Update the call in `main.py` to:
> `payment1 = MpesaPayment("0712345678", rental1)`

## Basic Usage

The demo can also be adapted in a Python script. Core objects are imported directly from the modules:

```python
from vehicle import EconomyCar
from customer import Customer
from rental_system import CarRentalSystem

system = CarRentalSystem("SafariDrive Rentals")

vehicle = EconomyCar("KDK 123A", "Toyota", "Axio", 2022, 4000)
customer = Customer("C001", "John Kamau", "0712345678", "12345678", "DL45821")

system.add_vehicle(vehicle)
system.register_customer(customer)
rental = system.rent_vehicle(customer, vehicle, 4)

print(vehicle.calculate_rental_cost(4))
print(rental.calculate_total())
```

## Payment Examples

The payment classes require the rental as their second argument for M-Pesa and as the first keyword argument for card and cash payments:

```python
from payment import MpesaPayment, CardPayment, CashPayment

mpesa = MpesaPayment("0712345678", rental)
card = CardPayment(card="41236789", rental=rental)
cash = CashPayment(cash=50000, rental=rental)
```

Each `process_payment()` method prints its result. `CashPayment.process_payment()` reports insufficient cash or returns the calculated change when the supplied amount is greater than the rental total.
