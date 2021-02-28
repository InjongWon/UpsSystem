"""
Question [12 marks]

In this question, you will complete a program for a car rental system that
allows renters to rent vehicles from rental companies.
- A renter has a name (str) and the total number of rentals they have ever
  made (int).
- A rental vehicle has an id (int) and description (str). If currently rented
  out, it stores the duration of the rental in days (int), and the name of its
  current renter (str); if not currently rented, both of these are None.
- A rental company has a name (str) and the vehicles that it owns.
You will need to write one class for each of these entities.

In the __main__ block below is an example of how we want to use these
classes. Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.  Any unspecified
behaviour is up to you -- it will not be tested.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool may be public, but all other attributes must be
private. You may add imports from the typing module, but do NOT add any other
imports.

Your code will be marked for correctness and design, as well as for having
class docstrings that follow the Class Design Recipe. Docstrings for your
methods are NOT required.

Save your solution in a file called Q5_solution.py and submit it on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from __future__ import annotations
from typing import List

# TODO: Define the 3 necessary classes here.

class RentalCompany:

    def __init__(self, name:str)->None:
        self.name = name
        self.vehicle = []
        self.rented = []

    def register_vehicles(self, vec: List[Rental]) -> None:
        self.vehicle.extend(vec)

    def get_rented_vehicles(self):
        return self.vehicle

    def rent_vehicle(self, renter: Renter, rental: Rental, duration: int) -> None:
        renter.num_rentals += 1
        rental.duration = duration
        rental.current_renter = renter
        self.rented.append(rental)

    def return_vehicle(self, renter: Renter, rental: Rental) -> None:
        rental.duration = None
        rental.current_renter = None
        self.rented.remove(renter)

    def get_rented_vehicles(self):
        return self.rented


class Renter:

    def __init__(self, name: str) -> None:
        self.name = name
        self.num_rentals = 0


class Rental:
    def __init__(self, vec_id: int, desc: str) -> None:
        self.vec_id = vec_id
        self.desc = desc
        self.duration = None
        self.current_renter = None


if __name__ == "__main__":
    # Instantiate a rental company
    company = RentalCompany('Top Rentals')

    # Instantiate two renters
    jessie = Renter('Jessie')
    gary = Renter('Gary')

    # Associate three rental vehicles with Top Rentals
    raptor = Rental(10821, '2020 Ford Raptor')
    bike = Rental(64933, 'Pink Bicycle')
    corolla = Rental(22345, '1996 Corolla')
    company.register_vehicles([raptor, bike, corolla])

    # Gary rents the bike for 1 day, Jessie rents the raptor for 23 days,
    # and Jessie also rents the corolla for 7 days
    company.rent_vehicle(gary, bike, 1)
    company.rent_vehicle(jessie, raptor, 23)
    company.rent_vehicle(jessie, corolla, 7)

    for vehicle in company.get_rented_vehicles():
        print(vehicle)
    # The output of the print statements is listed below. Notice that the order
    # is the same as the order in which vehicles were registered to the company.
    # 2020 Ford Raptor has been rented by Jessie for 23 day(s)
    # Pink Bicycle has been rented by Gary for 1 day(s)
    # 1996 Corolla has been rented by Jessie for 7 day(s)

    # Jessie returns the 1996 Corolla
    # company.return_vehicle(jessie, corolla)

    # Jessie attempts to return the Pink Bicycle
    # This does nothing because Gary is renting it, not Jessie.
    # company.return_vehicle(jessie, bike)

    # Jessie attempts to return the 1996 Corolla again.
    # This does nothing since she already returned it.
    # company.return_vehicle(jessie, corolla)

    # The 1996 Corolla was successfully returned
    assert corolla not in company.get_rented_vehicles()
    # The 2020 Ford Raptor remains rented
    assert raptor in company.get_rented_vehicles()
    # The Pink Bicycle remains rented to Gary
    assert bike in company.get_rented_vehicles() and \
           bike.current_renter is gary.name

    # Jessie has had 2 rentals in total and Gary has had 1 rental.
    assert jessie.num_rentals == 2
    assert gary.num_rentals == 1
