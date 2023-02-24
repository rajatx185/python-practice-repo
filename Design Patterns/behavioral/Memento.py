"""
The Memento design pattern is a behavioral pattern that provides the ability to restore an object to its previous state (undo via rollback). It is implemented by capturing the object's state into a memento object, and then storing the memento. Later, the state can be restored by passing the memento object back to the object.
"""
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

class CareTaker:
    def __init__(self, originator):
        self._mementos = []
        self._originator = originator

    def backup(self):
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save_to_memento())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_state()}")
        try:
            self._originator.restore_from_memento(memento)
        except Exception as e:
            self.undo()

if __name__ == "__main__":
    originator = Originator("Super-state")
    caretaker = CareTaker(originator)

    caretaker.backup()
    originator.set_state("State #1")
    caretaker.backup()
    originator.set_state("State #2")
    caretaker.backup()
    originator.set_state("State #3")
    caretaker.backup()
    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()
    caretaker.undo()
    caretaker.undo()

"""
In this example, the Originator class captures its state in the Memento class, the Caretaker class holds multiple Memento objects and can restore the Originator to a previous state by passing the appropriate Memento object to it.

It's the rollback pattern
- transacation
- undo
- git

whenever you want to restore to a previous state
"""