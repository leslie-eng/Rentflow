available = self.get_available_vehicles(vehicle_type=vehicle)
       if not available:
           raise ValueError(f"All the {vehicle} vehicles have been rented")
       
       vehicle = available[0]
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