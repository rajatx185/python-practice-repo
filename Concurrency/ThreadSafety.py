from threading import Thread
import sys
import threading

## Thread Unsafe Class
"""
Take a minute to go through the following program. It increments an object of class Counter using 5 threads. Each thread increments the object a hundred thousand times. The final value of the counter should be half a million (500,000). If you run the program enough times, you'll sometimes get the correct summation, and at others, you'll get an incorrect value.
"""

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()   

    def increment(self):
        # with self.lock:
            for _ in range(100000):
                self.lock.acquire()
                self.count += 1
                self.lock.release()

if __name__ == "__main__":
    
    # Sets the thread switch interval
    sys.setswitchinterval(0.005)

    numThreads = 5
    threads = [0] * numThreads
    counter = Counter()

    for i in range(0, numThreads):
        threads[i] = Thread(target=counter.increment)

    for i in range(0, numThreads):
        threads[i].start()

    for i in range(0, numThreads):
        threads[i].join()

    if counter.count != 500000:
        print(" count = {0}".format(counter.count), flush=True)
    else:
        print(" count = 500000 - Try re-running the program.")

## Fixing Thread Unsafe Class
