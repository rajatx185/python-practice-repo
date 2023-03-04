"""
compute the sum of all the integers from 0 to 300000000 (30 million).
"""
from threading import Thread
from multiprocessing import Process
from multiprocessing.managers import BaseManager
from queue import Queue
import time
import multiprocessing

class SumUpClass:
    def __init__(self) -> None:
        self.__counter = 0
    
    def add_integers(self, start, end):
        for i in range(start, end+1):
            self.__counter += i
    
    def get_counter(self):
        return self.__counter

def single_thread():
    obj = SumUpClass()
    start = time.time()
    obj.add_integers(1, 3000000)
    end = time.time()
    execution_time = end - start
    print("single threaded took : {} seconds and summed to {}".format(execution_time, obj.get_counter()))

def multi_thread():
    obj1 = SumUpClass()
    obj2 = SumUpClass()
    start = time.time()

    t1 = Thread(target=obj1.add_integers, args=(1,1500000))
    t2 = Thread(target=obj2.add_integers, args=(1500001, 3000000))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    combined_sum = obj1.get_counter() + obj2.get_counter()
    end = time.time()
    execution_time = end - start
    print("multi threaded took : {} seconds and summed to {}".format(execution_time, combined_sum))

def single_process(obj1, start, end):
    obj1.add_integers(start, end)

def multiple_processes():
    BaseManager.register('SumUpClass', SumUpClass)
    manager = BaseManager(address=('127.0.0.1', 63333))
    manager.start()

    obj1 = manager.SumUpClass()
    obj2 = manager.SumUpClass()
    start = time.time()

    p1 = Process(target=single_process, args=(obj1, 1, 15000000,))
    p2 = Process(target=single_process, args=(obj2, 15000001, 30000000,))

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()

    combined_sum = obj1.get_counter() + obj2.get_counter()
    end = time.time() - start
    print("multiple processes took : {} seconds and summed to {}".format(end, combined_sum))
    manager.shutdown()

if __name__ == "__main__":
    print("System has {0} CPUs".format(multiprocessing.cpu_count()))
    single_thread()
    multi_thread()
    multiple_processes()

"""
The results are interesting and counterintuitive. We would expect the multithreaded scenario to perform better than the single-threaded one since two threads can work in parallel if the system has at least two CPUs. The relatively poor performance in comparison to the single-threaded scenario can be explained by (standard) Python's Achilles’ heel, the Global Interpreter Lock, an entity within the Python framework that allows a single thread to execute even in the presence of more than one idle CPUs. We'll have more to say on that subject in later sections. Multithreaded scenarios may not experience any performance gains in case of CPU-intensive tasks such as the one in our example because threads don't execute in parallel and in fact incur an additional cost of management and coalescing partial results.

With multiple processes we can expect each process to be scheduled onto a separate CPU and work in parallel. However, there's the additional overhead of creating and tearing down processes, which is higher than doing the same for threads. Additionally, we utilize Python's inter-process communication machinery, which uses the proxy-pattern and adds network latency to the multiprocessing scenario. Collectively these headwinds explain why the multiprocessing scenario performs no better than a single-threaded scenario.

However, in general tasks involving blocking operations such as network and disk I/O, can see significant performance gains when migrated to a multithreaded or multiprocessor architecture.
"""