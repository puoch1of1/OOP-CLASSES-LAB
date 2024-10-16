# this is the code for the garage class

from vehicleClass import Vehicle

class Garage:
    def __init__(self):
        self.parked_vehicle = None
    def parkVehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.parked_vehicle = vehicle

    def toString(self):
        if self.parked_vehicle:
            return f"Description of the parked vehicle:\n{self.parked_vehicle.toString()}"
        else:
            return "The garage is empty."

#example output
from carClass import Car
from truckclass import Truck

my_car1 = Car("blue", winter_tires=True)
my_truck = Truck("green", has_trailer=True)

#park the car in the garage
my_garage = Garage()
my_garage.parkVehicle(my_car1)
print(my_garage.toString())