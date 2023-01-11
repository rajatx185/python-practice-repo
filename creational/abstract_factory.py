from abc import ABC, abstractmethod
"""
Factory of Factory
"""
### Product Interface ###
class Vehicle(ABC):
    @abstractmethod
    def average(self):
        pass

#### Product Concrete Class ###
class BMW(Vehicle):
    def average(self):
        print("10")

class Maruti(Vehicle):
    def average(self):
         print("20")

class Mercedes(Vehicle):
    def average(self):
         print("15")

###### Vehicle Factory Interface ######
class VehicleFactory(ABC):
    @abstractmethod
    def get_vehicle(self):
        pass

#### Vehicle Factory Concrete Classes ####
class LuxuryFactory(VehicleFactory):
    def get_vehicle(self, input):
        if input == "BMW":
            return BMW()
        elif input == "Mercedes":
            return Mercedes()
        else:
            return None

class OrdinaryFactory(VehicleFactory):
    def get_vehicle(self, input):
        if input == "Maruti":
            return Maruti()
        else:
            return None

### Factory for vehicle factory ####
class VehicleFactoryFactory:
    def get_vehicle_factory(self, input):
        if input in ["Luxury"]:
            return LuxuryFactory()
        elif input in ["Ordinary"]:
            return OrdinaryFactory()

### client code ####
vff = VehicleFactoryFactory()
lvf = vff.get_vehicle_factory(input="Luxury")
ovf = vff.get_vehicle_factory(input="Ordinary")
bmw_car = lvf.get_vehicle(input="BMW")
bmw_car.average()
maruti_car = ovf.get_vehicle(input="Maruti")
maruti_car.average()
merc_car = lvf.get_vehicle(input="Mercedes")
merc_car.average()