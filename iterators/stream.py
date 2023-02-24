"""
Stream Iterators: These iterators allow you to read and write elements from and to a stream, such as a file or a network socket.
"""
class StreamIterator:
    def __init__(self, file_path, chunk_size=1024):
        self.file = open(file_path, "rb")
        self.chunk_size = chunk_size
        
    def __iter__(self):
        return self
    
    def __next__(self):
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            raise StopIteration
        return chunk
    
    def __del__(self):
        self.file.close()

for chunk in StreamIterator("example.txt"):
    print(chunk)

"""
This will print the contents of the file in chunks of 1024 bytes, or less if the file is smaller than that. Note that the __del__ method is called automatically when the iterator is garbage collected, which ensures that the file is closed properly even if the iteration is stopped early.
"""