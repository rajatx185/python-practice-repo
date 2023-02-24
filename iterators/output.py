class OutputIterator:
    def __init__(self):
        self.data = []
    
    def write(self, value):
        self.data.append(value)
        
    def __iter__(self):
        for item in self.data:
            yield item

output = OutputIterator()
output.write(1)
output.write(2)
output.write(3)
for i in output:
    print(i)

"""
In the __iter__ method of the OutputIterator class, the yield statement is used to return values one by one, instead of returning the entire sequence at once. The yield keyword allows the __iter__ method to behave like a generator function.

When the for loop starts to iterate over output, the __iter__ method is called, which starts executing from the first line of the method. When it encounters the yield statement, the generator function yields the current value of item and suspends its execution. The for loop continues with the next iteration, calling the __iter__ method again, which picks up right where it left off, and yields the next value in the sequence. This continues until there are no more values left to yield, at which point the __iter__ method raises StopIteration to signal the end of the iteration.

The use of yield in this case makes it more memory-efficient, because it allows you to iterate over large sequences of data without having to load the entire sequence into memory at once.
"""