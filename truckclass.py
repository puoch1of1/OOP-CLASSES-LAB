
#this is the third code for the truck class

from vehicleClass import Vehicle


class Truck(Vehicle):
    def __init__(self, color,  has_trailer=False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        vehicle_string = super().toString()
        trailer_string = f"Has trailer: {self.has_trailer}"
        return f"{vehicle_string}\n{trailer_string}"

#example code
this_truck = Truck("blue", has_trailer=True)
print(this_truck.getColor())
print(this_truck.toString())