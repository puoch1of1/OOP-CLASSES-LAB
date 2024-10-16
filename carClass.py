#this is the second part of the assignment


from vehicleClass import Vehicle, this_vehicle


class Car(Vehicle):
    def __init__(self, color, winter_tires = False):
        super().__init__(color)
        self.winter_tires = winter_tires

    def toString(self):
        vehicle_string = super().toString()
        tires_string = f"has winter tires: {self.winter_tires}"

#example
another_vehicle = Car("silver", winter_tires=True)
print(another_vehicle.getColor())
print(another_vehicle.toString())