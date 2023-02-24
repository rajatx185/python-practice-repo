"""
The Visitor design pattern is a behavioral design pattern that allows adding new behaviors to existing objects without modifying the objects themselves. It separates the algorithms from the objects on which they operate.

A real-world example of visitor pattern could be a tax calculation scenario. You have a list of items and each item has a different price and type. You want to calculate the total tax amount for all the items. Instead of adding tax calculation logic to each item class, you can use visitor pattern where you create a visitor class that calculates tax for different types of items and then visit each item to calculate the total tax.

Here is a python code snippet for a visitor pattern implementation:
"""

# https://refactoring.guru/design-patterns/visitor


from abc import ABC, abstractmethod

class TaxVisitor(ABC):
    @abstractmethod
    def visit(self, item):
        pass

class TaxHolidayVisitor(TaxVisitor):
    def visit(self, item):
        return item.price * 0.10

class TaxLuxuryVisitor(TaxVisitor):
    def visit(self, item):
        return item.price * 0.15

class Item(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def accept(self, visitor):
        pass

class HolidayItem(Item):
    def accept(self, visitor):
        return visitor.visit(self)

class LuxuryItem(Item):
    def accept(self, visitor):
        return visitor.visit(self)

items = [HolidayItem(100), LuxuryItem(200), HolidayItem(50), LuxuryItem(300)]

tax_holiday_visitor = TaxHolidayVisitor()
tax_luxury_visitor = TaxLuxuryVisitor()

total_tax = 0
for item in items:
    total_tax += item.accept(tax_holiday_visitor if isinstance(item, HolidayItem) else tax_luxury_visitor)

print("Total Tax:", total_tax)
