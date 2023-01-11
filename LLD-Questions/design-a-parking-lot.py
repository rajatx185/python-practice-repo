"""
Requirements Gathering
- How many entrances? 1
- How many exits? 1
- What are different types of spots? 2-wheeler, 4-wheeler
- How to charge? hour-based, minute-based - mixed
- How to accept payment? cash, online
- Parking spot should be nearest to the entrance
- How many parking floors? 1

Objects
- Vehicle(vehicle-number, vehicle-type[enum])
- Ticket(entry-time, parking-spot)
- Entrance Gate(find_parking_space, update_parking_space, generate_ticket)
- Exit Gate(cost_calculation, collect_payment, update_parking_spot)
- Parking Spot(number, is_empty, vehicle, price, type)

Design Approaches
- Top Down
- Bottom Up
"""

"""
solution
https://github.com/GauravGuptaDeveloper/ParkingLot
"""

from abc import ABC, abstractmethod

### Parking Spot Class ###
class ParkingSpot:
    def __init__(self, id, vehicle, price) -> None:
        self._id = id
        self._is_empty = True
        self._vehicle = vehicle
        self._price = price
    
    @property
    def id(self):
        return self._id

    # @property.setter
    # def id(self, id):
    #     self._id = id

    def park(self):
        pass

    def unpark(self):
        pass

### Two Wheeler Parking Spot Class ###
class TwoWheelerParkingSpot(ParkingSpot):
    pass

### Four Wheeler Parking Spot Class
class FourWheelerParkingSpot(ParkingSpot):
    pass

### Parking Spot Manager Class ###
class ParkingSpotManager:
    def __init__(self, parking_spots) -> None:
        self.parking_spots = parking_spots
    
    def find_parking_spot(self):
        pass

    def add_parking_spot(self):
        pass

    def remove_parking_spot(self):
        pass
    
    def park_vehicle(self,vehicle):
        pass

    def unpark_vehicle(self,vehicle):
        pass

class TwoWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots) -> None:
        super.__init__(parking_spots)

class FourWheelerParkingSpotManager(ParkingSpotManager):
    def __init__(self, parking_spots) -> None:
        super.__init__(parking_spots)
    
### Strategy for finding a parking spot ###
class ParkingSpotStrategy(ABC):
    @abstractmethod
    def find_spot(self):
        pass

class NearestToEntranceStrategy(ParkingSpotStrategy):
    def find_spot(self):
        pass

class NearestToElevator(ParkingSpotStrategy):
    def find_spot(self):
        pass

### Vehicle ####
class Vehicle:
    def __init__(self, number, type) -> None:
        self.number = number
        self.type = type

### Ticket ###
class Ticket:
    def __init__(self,entry_time,vehivle,parking_slot) -> None:
        pass

### Entrance Gate ####
class EntranceGate:
    def __init__(self, parking_spot_factory) -> None:
        self.parking_spot_manager = None

    def find_parking_space(self, vehicle, entrance_gate_no):
        pass
    
    def book_spot(self):
        pass

    def generate_ticket(self):
        pass
### class ParkingManagerFactory ###
class ParkingSpotManagerFactory:
    def get_parking_spot_manager(self, vehicle_type):
        pass


## Exit Gate ###
class ExitGate:
    pass

### Cost Computation ###
class CostComputation(ABC):
    @abstractmethod
    def cost(self, strtegy):
        pass

class TwoWheelerCostComputation(CostComputation):
    def cost(self):
        pass

class FourWheelerCostComputation(CostComputation):
    def cost(self):
        pass

### Pricing Strategy ####
class PricingStrategy(ABC):
    @abstractmethod
    def price(self, ticket):
        pass

class HourlyPricingStrategy(PricingStrategy):
    def price(self, ticket):
        return 


### Cost computation Factory ###