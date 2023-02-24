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


### Example 2
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount: int):
        print(f"Paying {amount} using credit card")

class PayPalPayment(Payment):
    def pay(self, amount: int):
        print(f"Paying {amount} using PayPal")

class CashPayment(Payment):
    def pay(self, amount: int):
        print(f"Paying {amount} in cash")

class Purchase:
    def __init__(self, payment: Payment):
        self.payment = payment

    def pay(self, amount: int):
        self.payment.pay(amount)

purchase = Purchase(CashPayment())
purchase.pay(100)

"""
In this example, the Purchase class accepts an object that implements the Payment interface. The Purchase class can use different payment strategies, such as credit card, PayPal, or cash, without having to know the details of the specific payment method. The Pay method is defined in the Payment class and is implemented by the different payment strategies.

"""