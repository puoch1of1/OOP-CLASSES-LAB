from truckclass import Truck
from garageClass import Garage, my_garage


class GarageTester:
    @staticmethod
    def getExample():
        my_truck1 = Truck ("black", has_trailer=False)

        my_garage1 = Garage()

        my_garage1.parkVehicle(my_truck1)

        print(my_garage1.toString())

GarageTester.getExample()