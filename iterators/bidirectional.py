"Bidirectional Iterators: These iterators allow you to traverse a collection of elements in both forward and backward directions."

class BidirectionalIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            result = self.data[self.index]
            self.index -= 1
            return result

    def previous(self):
        if self.index >= len(self.data) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.data[self.index]

my_iterator = BidirectionalIterator([1, 2, 3, 4, 5])

# Forward iteration:
print("Forward iteration:")
for x in my_iterator:
    print(x)

# Backward iteration:
print("Backward iteration:")
for x in reversed(my_iterator):
    print(x)
