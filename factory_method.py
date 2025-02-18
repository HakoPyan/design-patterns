from abc import ABC, abstractmethod
from enum import Enum

# Simple implementation (not GoF variant which says that each class should have its own factory)


# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"


# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    def get_name(self) -> str:
        return VehicleType.CAR.value


class Motorcycle(Vehicle):
    def get_name(self) -> str:
        return VehicleType.MOTORCYCLE.value


class Bicycle(Vehicle):
    def get_name(self) -> str:
        return VehicleType.BICYCLE.value


# Step 3: Create a VehicleFactory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        vehicles_by_types = {
            VehicleType.CAR: Car,
            VehicleType.BICYCLE: Bicycle,
            VehicleType.MOTORCYCLE: Motorcycle,
        }
        _class = vehicles_by_types.get(vehicle_type)
        if _class:
            return _class()
        raise TypeError('No such type')


# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())


if __name__ == "__main__":
    main()
