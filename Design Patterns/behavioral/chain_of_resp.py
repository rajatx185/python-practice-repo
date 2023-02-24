"""
The Chain of Responsibility design pattern is a behavioral design pattern that allows multiple objects to handle a request in a chain-like manner. The idea behind this pattern is that a request can be passed from one object to another until it is handled.

A real-world example of the Chain of Responsibility pattern could be an ATM machine dispensing cash. When a customer requests cash, the request is first passed to the ATM's highest-denomination cash dispenser. If that dispenser doesn't have sufficient cash, the request is passed to the next-highest dispenser, and so on, until the request is either fulfilled or rejected because none of the dispensers have sufficient cash.
"""
class Dispenser:
    def __init__(self, next_dispenser=None):
        self.next_dispenser = next_dispenser

    def dispense(self, cash_request):
        if self.can_dispense(cash_request):
            self.do_dispense(cash_request)
        elif self.next_dispenser:
            self.next_dispenser.dispense(cash_request)
        else:
            print("Sorry, cannot dispense that amount")

    def can_dispense(self, cash_request):
        raise NotImplementedError

    def do_dispense(self, cash_request):
        raise NotImplementedError

class Rupee500Dispenser(Dispenser):
    def can_dispense(self, cash_request):
        return cash_request >= 500

    def do_dispense(self, cash_request):
        num = cash_request // 500
        cash_request -= num * 500
        print("Dispensed 500 * " + str(num))
        return cash_request

class Rupee100Dispenser(Dispenser):
    def can_dispense(self, cash_request):
        return cash_request >= 100

    def do_dispense(self, cash_request):
        num = cash_request // 100
        cash_request -= num * 100
        print("Dispensed 100 * " + str(num))
        return cash_request

# Build the dispenser chain:
atm = Rupee500Dispenser(Rupee100Dispenser())
atm.dispense(3020)

"""
In this example, the dispense method checks if it can fulfill the request by calling can_dispense and if it can, dispenses the cash by calling do_dispense. If it can't, it passes the request to the next dispenser in the chain.
"""


class DispenseChain:
    def __init__(self, next_chain=None):
        self._next_chain = next_chain

    def set_next(self, next_chain):
        self._next_chain = next_chain

    def dispense(self, currency):
        pass

class Dollar50Dispenser(DispenseChain):
    def dispense(self, currency):
        if currency >= 50:
            num = currency // 50
            remainder = currency % 50
            print("Dispensing {} 50$ note(s)".format(num))
            if remainder != 0:
                self._next_chain.dispense(remainder)
        else:
            self._next_chain.dispense(currency)

class Dollar20Dispenser(DispenseChain):
    def dispense(self, currency):
        if currency >= 20:
            num = currency // 20
            remainder = currency % 20
            print("Dispensing {} 20$ note(s)".format(num))
            if remainder != 0:
                self._next_chain.dispense(remainder)
        else:
            self._next_chain.dispense(currency)

class Dollar10Dispenser(DispenseChain):
    def dispense(self, currency):
        if currency >= 10:
            num = currency // 10
            remainder = currency % 10
            print("Dispensing {} 10$ note(s)".format(num))
            if remainder != 0:
                self._next_chain.dispense(remainder)
        else:
            self._next_chain.dispense(currency)

# Build the chain of dispensers
dollar50 = Dollar50Dispenser()
dollar20 = Dollar20Dispenser()
dollar10 = Dollar10Dispenser()

dollar50.set_next(dollar20)
dollar20.set_next(dollar10)

# Currency to be dispensed
currency = int(input("Enter amount to be dispensed: "))
dollar50.dispense(currency)

"""
In this example, DispenseChain is an interface that defines the structure for each dispenser in the chain. The Dollar50Dispenser, Dollar20Dispenser, and Dollar10Dispenser classes implement the dispense method to handle different denominations of banknotes, and the set_next method to link the dispensers in the chain. The dispensers are linked together to form the chain, and the dispense method of the first dispenser in the chain is called with the currency amount to be dispensed. The chain of dispensers works until the entire amount has been dispensed in the smallest possible denomination of banknotes.
"""