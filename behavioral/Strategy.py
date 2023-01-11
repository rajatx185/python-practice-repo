"""
is a relationship is inheritance
has a is composition
"""
### create the following interface DriveStrategy
### create concrete class using the DriveStrategy interface
### create a vehicle parent class that has the above interface
### create a vehicle child class that extends the parent class

from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass

class SportDriveStrategy(DriveStrategy):
    def drive(self):
        print("My Drive Strategy is sport")

class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print("My Drive Strategy is normal")

class Vehicle:
    def __init__(self, strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy
    
    @strategy.setter
    def strategy(self,strategy):
        self._strategy = strategy

    def drive(self):
        self._strategy.drive()

class SportVehicle(Vehicle):
    def __init__(self, strategy) -> None:
        super().__init__(strategy)

if __name__ == "__main__":
    obj = SportVehicle(NormalDriveStrategy())
    obj.drive()
