
# this is the first part of the lab

class Vehicle:
    def __init__(self, color):  #initialize the color instance
        self.color = color
    def getColor(self):
        return self.color #return the color of the vehicle
    def toString(self):
        return f"This vehicle is {self.color}" # to output the string with the color

this_vehicle = Vehicle("yellow")
print(this_vehicle.getColor())
print(this_vehicle.toString())