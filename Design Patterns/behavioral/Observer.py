"""
LLD Question
- Implement notify me when product is out of stock on Amazon like websites
"""
"""
Observer Pattern
Entities: observable, observer 
Logic:  when the state of observable changes, it updates the observer
"""

from abc import ABC, abstractmethod

### observable code ###
class ProductStockObservale(ABC):
    @abstractmethod
    def add(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setStockCount(self, new_stock_added):
        pass

    @abstractmethod
    def getStockCount(self):
        pass

class IphoneStockObservable(ProductStockObservale):
    def __init__(self) -> None:
        self.stock = 0
        self.observer_list = set()

    def add(self, observer):
        self.observer_list.add(observer)
    
    def remove(self, observer):
        self.observer_list.discard(observer)

    def notify(self):
        for observer in self.observer_list:
            observer.update()

    def setStockCount(self, new_stock_added):
        if self.stock == 0:
            self.notify()
        self.stock += new_stock_added

    def getStockCount(self):
        return self.stock

### observer code ### 
class NotificationAlertObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class EmailAlertObserver(NotificationAlertObserver):
    def __init__(self, email, observable) -> None:
        self.observable = observable
        self.email = email

    def update(self):
        print(f"email alert sent to {self.email}")

class MobileAlertObserver(NotificationAlertObserver):
    def __init__(self, username, observable) -> None:
        self.observable = observable
        self.username = username

    def update(self):
        print(f"mobile alert sent to {self.username}")

if __name__ == "__main__":
    iphone_stock_observable_obj = IphoneStockObservable()
    observer1 = EmailAlertObserver(email="rajat.g@pharmeasy.in", observable=iphone_stock_observable_obj)
    observer2 = EmailAlertObserver(email="kriti.g@pharmeasy.in", observable=iphone_stock_observable_obj)
    observer3 = MobileAlertObserver(username="suresh.g", observable=iphone_stock_observable_obj)
    iphone_stock_observable_obj.add(observer1)
    iphone_stock_observable_obj.add(observer2)
    iphone_stock_observable_obj.add(observer3)
    iphone_stock_observable_obj.setStockCount(10)
    iphone_stock_observable_obj.setStockCount(-10)
    iphone_stock_observable_obj.setStockCount(10)